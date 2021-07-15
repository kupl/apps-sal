#!/usr/bin/env python3

import sys
import traceback

class Input(object):
    def __init__(self):
        self.fh = sys.stdin

    def next_line(self):
        while True:
            line = sys.stdin.readline()
            if line == '\n':
                continue
            return line


    def next_line_ints(self):
        line = self.next_line()
        return [int(x) for x in line.split()]

    def next_line_strs(self):
        line = self.next_line()
        return line.split()

def get_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def calculate_finish_cost(dp_reach, points):
    """ Return dp_finish of this level. """
    assert len(dp_reach) == len(points)
    if len(points) == 1:
        return dp_reach
    round_cost = get_dist(points[0], points[-1])
    # dp_finish = min(2 * round_cost + (dp[p1] - dist)). omit 2 * round_cost for now.
    dp_finish = dp_reach[:]
    min_diff = dp_reach[0]
    for i in range(1, len(points)):
        min_diff = min(min_diff - get_dist(points[i], points[i-1]), dp_reach[i])
        dp_finish[i] = min(min_diff, dp_finish[i])
    min_diff = dp_reach[-1]
    for i in range(len(points) - 2, -1, -1):
        min_diff = min(min_diff - get_dist(points[i], points[i+1]), dp_reach[i])
        dp_finish[i] = min(min_diff, dp_finish[i])
    assert len(dp_finish) == len(points)
    return [x + 2 * round_cost for x in dp_finish]

def calculate_reach_cost(dp_finish, from_points, to_points):
    """calculate from dp_finish of current level to the dp_reach of the next level."""
    assert len(dp_finish) == len(from_points)
    from_k = [y/max(x, 0.5) for x, y in from_points]
    to_k = [y/max(x, 0.5) for x, y in to_points]
    dp_reach = []
    from_index = 0
    for i in range(len(to_points)):
        while from_index + 1 < len(from_points) and from_k[from_index + 1] > to_k[i]:
            from_index += 1
        dp = dp_finish[from_index] + get_dist(from_points[from_index], to_points[i])
        if from_index + 1 < len(from_points):
            dp = min(dp, dp_finish[from_index + 1] + get_dist(from_points[from_index + 1], to_points[i]))
        dp_reach.append(dp)
    assert len(dp_reach) == len(to_points)
    return dp_reach


def get_min_dist(points):
    # 1. split points into levels, sort points in each level in x increase, y decrease order.
    level_dict = {}
    for point in points:
        level = max(point[0], point[1])
        if level in level_dict:
            level_dict[level].append(point)
        else:
            level_dict[level] = [point]
    level_points = []
    for level in sorted(level_dict.keys()):
        p = level_dict[level]
        level_points.append(sorted(p, key=lambda x: x[0] - x[1]))

    # 2. calculate the min cost to reach a level at a point.
    #    calculate the min cost to finish a level at a point.
    dp_reach = []
    for p in level_points[0]:
        dp_reach.append(p[0] + p[1])
    dp_finish = calculate_finish_cost(dp_reach, level_points[0])
    for i in range(len(level_points) - 1):
        from_points = level_points[i]
        to_points = level_points[i + 1]
        dp_reach = calculate_reach_cost(dp_finish, from_points, to_points)
        dp_finish = calculate_finish_cost(dp_reach, to_points)

    # 3. the result is to finish at any points at the last level.
    return min(dp_finish)

def main():
    input = Input()
    while True:
        try:
            nums = input.next_line_ints()
            if not nums:
                break
            n = nums[0]
            points = []
            for _ in range(n):
                x, y = input.next_line_ints()
                points.append((x, y))
        except:
            print('read input failed')
        try:
            min_dist = get_min_dist(points)
        except:
            traceback.print_exc(file=sys.stdout)
            print('get_min_dist failed')
        print("{}".format(min_dist))

main()
