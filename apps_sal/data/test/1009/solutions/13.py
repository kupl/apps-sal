"""
Codeforces Round #334 (Div. 2)

Problem 604 B. More Cowbell

@author yamaton
@date 2015-12-01
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs, n, k):
    if k >= n:
        return max(xs)
    ys1 = xs[:(n - k)]
    ys2 = xs[(n - k) : 2*(n - k)]
    maxval = max(a + b for (a, b) in zip(ys1, ys2[::-1]))
    return max(maxval, xs[-1])

# def pp(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n, k = list(map(int, input().split()))
    xs = [int(c) for c in input().split()]
    assert len(xs) == n
    result = solve(xs, n, k)
    print(result)


def __starting_point():
    main()

__starting_point()
