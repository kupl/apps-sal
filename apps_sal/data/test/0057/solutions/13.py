"""
Codeforces Round #331 (Div. 2)

Problem 596 A

@author yamaton
@date 2015-11-15
"""
import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(pairs, n):
    if n <= 1:
        return -1
    elif n == 2:
        (a, b) = pairs[0]
        (c, d) = pairs[1]
        if a == c or b == d:
            return -1
        else:
            return abs(a - c) * abs(b - d)
    elif n >= 3:
        xmin = min((x for (x, _) in pairs))
        xmax = max((x for (x, _) in pairs))
        ymin = min((y for (_, y) in pairs))
        ymax = max((y for (_, y) in pairs))
        return (xmax - xmin) * (ymax - ymin)


def main():
    n = int(input())
    pairs = [tuple((int(_c) for _c in input().strip().split())) for _ in range(n)]
    assert len(pairs[0]) == 2
    result = solve(pairs, n)
    print(result)


def __starting_point():
    main()


__starting_point()
