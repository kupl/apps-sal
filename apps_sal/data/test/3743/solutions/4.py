3

import array
import bisect
import collections
from fractions import Fraction
import functools
import itertools
import math
import os
import sys


def main():
    N = read_int()
    print(solve(N))


def solve(N):
    d = []
    x = 2
    while x * x <= N:
        if N % x == 0:
            d.append(x)
            if x * x < N:
                d.append(N // x)
        x += 1

    d.sort()
    if not d:
        return N
    g = d[0]
    for x in d[1:]:
        g = math.gcd(g, x)
    return g


###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def __starting_point():
    main()

__starting_point()
