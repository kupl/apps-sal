"""
Codeforces Round #330 (Div. 2)

Problem 595 B

@author yamaton
@date 2015-11-08
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

BASE = 1000000007


def count(k, a, b):
    x = count_multiples(a, 0, 10**k - 1)
    y = count_multiples(a, b * 10**(k - 1), (b + 1) * 10**(k - 1) - 1)
    return x - y


def count_multiples(a, _from, _to):
    if _from == 0:
        return _to // a - (_from - 1) // a
    else:
        return _to // a - (_from - 1) // a


def solve(xs, ys, n, k):
    result = 1
    for (a, b) in zip(xs, ys):
        result = (result * count(k, a, b)) % BASE
    return result


def main():
    [n, k] = [int(i) for i in input().strip().split()]
    xs = [int(i) for i in input().strip().split()]
    ys = [int(i) for i in input().strip().split()]
    assert len(xs) == len(ys) == n // k
    result = solve(xs, ys, n, k)
    print(result)


def __starting_point():
    main()


__starting_point()
