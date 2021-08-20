"""
Solution to the 320B problem on CodeForces.

# pylint: disable = C0325
# pylint: disable = W0611
"""
from collections import deque


def filter_intervals(intv, input_list):
    """
    Filters the list for all the intervals that are valid.
    """
    return ((x, y) for (x, y) in input_list if int(intv[0]) > int(x) and int(intv[0]) < int(y) or (int(intv[1]) > int(x) and int(intv[1]) < int(y)))


def interval_search(intv, target, input_list):
    """
    Finds if a path exists from one interval to another.
    """
    visited = set()
    d = deque()
    d.append(intv)
    while d:
        intv = d.pop()
        if intv == target:
            return True
        if intv not in visited:
            visited.add(intv)
            for interval in filter_intervals(intv, input_list):
                if interval not in visited:
                    d.append(interval)
    return False


def main():
    """
    Docstring or main.
    """
    num_inputs = int(input())
    interval_list = []
    for _ in range(num_inputs):
        (input_type, beg, end) = input().split()
        beg = int(beg)
        end = int(end)
        if int(input_type) == 1:
            interval_list.append((beg, end))
        elif interval_search(interval_list[beg - 1], interval_list[end - 1], interval_list):
            print('YES')
        else:
            print('NO')


def __starting_point():
    main()


__starting_point()
