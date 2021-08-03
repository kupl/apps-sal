"""
Codeforces Educational Round

Problem 598 A Tricky Sum

@author yamaton
@date 2015-11-12
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(x):
    simple_sum = x * (x + 1) // 2

    pow = -1
    while x > 0:
        x >>= 1
        pow += 1

    sum_power_of_twos = 2**(pow + 1) - 1
    return simple_sum - 2 * sum_power_of_twos


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def main():
    t = int(input())
    xs = [int(input()) for _ in range(t)]

    results = [solve(x) for x in xs]
    for res in results:
        print(res)


def __starting_point():
    main()


__starting_point()
