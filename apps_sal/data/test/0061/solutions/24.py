"""
Codeforces Round 333 (Div. 2)

Problem 602 A.

@author yamaton
@date 2015-11-24
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs, ys, bx, by):
    x = functools.reduce(lambda acc, x: acc * bx + x, xs)
    y = functools.reduce(lambda acc, y: acc * by + y, ys)
    if x < y:
        return '<'
    elif x > y:
        return '>'
    else:
        return '='


# def p(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    [n, bx] = list(map(int, input().strip().split()))
    xs = [int(c) for c in input().strip().split()]
    assert len(xs) == n
    [m, by] = list(map(int, input().strip().split()))
    ys = [int(c) for c in input().strip().split()]
    assert len(ys) == m

    result = solve(xs, ys, bx, by)
    print(result)


def __starting_point():
    main()


__starting_point()
