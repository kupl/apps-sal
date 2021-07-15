"""
Codeforces Round 332

Problem 599 A. Patrick and Shopping

@author yamaton
@date 2015-11-20
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

BIGMOD = 1000000007


def solve(d1, d2, d3):
    return min(d1 + d2 + d3, 2*(d1 + d2), 2*(d1 + d3), 2*(d2 + d3))


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def main():
    [d1, d2, d3] = map(int, input().strip().split())
    result = solve(d1, d2, d3)
    print(result)


def __starting_point():
    main()

__starting_point()
