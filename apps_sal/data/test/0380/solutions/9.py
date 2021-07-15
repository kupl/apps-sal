#!/usr/bin/env python3
import operator
from itertools import islice
import math


def all_on_same_line(points):
    return all(x == points[0][0] for x, y in points) or all(y == points[0][1] for x, y in points)


def all_on_different_lines(points):
    return len(set(x for x, y in points)) == len(points) and len(set(y for x, y in points)) == len(points)


def has_two_points_with_same_x_coord(points):
    return len(set(x for x, y in points)) == 2


def get_common_x(points):
    xs = [x for x, y in points]
    for xx in set(x for x, y in points):
        if xs.count(xx) == 2:
            return xx

def get_common_y(points):
    ys = [y for x, y in points]
    for yy in set(y for x, y in points):
        if ys.count(yy) == 2:
            return yy


def main():
    points = [(int(x), int(y)) for x, y in (input().split() for _ in range(3))]
    if all_on_same_line(points):
        print(1)
    elif all_on_different_lines(points):
        print(3)
    else:
        if has_two_points_with_same_x_coord(points):
            y = get_common_x(points)
            points = sorted(points, key=lambda p: p[0] == y)
            if min(points[1][1], points[2][1]) < points[0][1] <  max(points[1][1], points[2][1]):
                print(3)
            else:
                print(2)
        else:
            y = get_common_y(points)
            points = sorted(points, key=lambda p: p[1] == y)
            if min(points[1][0], points[2][0]) < points[0][0] <  max(points[1][0], points[2][0]):
                print(3)
            else:
                print(2)


def __starting_point():
    main()

__starting_point()
