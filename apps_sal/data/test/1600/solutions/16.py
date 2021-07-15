"""
Codeforces Round #332

Problem 599 C. Day at the Beach

@author yamaton
@date 2015-11-20
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs, n):
    max_upto = list(it.accumulate(xs, max))
    min_after = list(it.accumulate(reversed(xs), min))
    min_after.reverse()
    count = 1 + sum(1 for i in range(1, n) if max_upto[i-1] <= min_after[i])
    return count


def solve_old(xs, n):
    max_upto = []
    maxval = 0
    for x in xs:
        maxval = max(maxval, x)
        max_upto.append(maxval)

    min_after = []
    minval = 10000000000
    for x in reversed(xs):
        minval = min(minval, x)
        min_after.append(minval)
    min_after.reverse()

    count = 1
    for i in range(1, n):
        if max_upto[i-1] <= min_after[i]:
            count += 1

    return count


#
# @functools.lru_cache(maxsize=None)
# def count(tup):
#     if len(tup) == 1:
#         return 1
#
#     maxval = 1
#     n = len(tup)
#     for i in range(1, n):
#         first = tup[:i]
#         second = tup[i:]
#         if max(first) <= min(second):
#             maxval = max(maxval, count(first) + count(second))
#     return maxval
#
#
# def solve(xs, n):
#     return count(tuple(xs))


# def p(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(_c) for _c in input().strip().split()]

    result = solve(xs, n)
    print(result)


def __starting_point():
    main()

__starting_point()
