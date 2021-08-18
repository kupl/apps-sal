"""
Codeforces Testing Round 

Problem 597A Divisibility

@author yamaton
@date 2015-11-11
"""

import math
import random
import sys

import functools


def solve(k, a, b):
    return b // k - (a - 1) // k


def p(*args, **kwargs):
    return print(file=sys.stderr, *args, **kwargs)


def main():
    [k, a, b] = [int(i) for i in input().strip().split()]
    result = solve(k, a, b)
    print(result)


def __starting_point():
    main()


__starting_point()
