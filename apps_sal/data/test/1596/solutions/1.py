3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys


def main():
    S = inp()
    print(solve(S))


MOD = 10 ** 9 + 7


def solve(S):
    N = len(S)
    fib = [0] * (N + 1)
    fib[0] = fib[1] = 1
    for i in range(2, N + 1):
        fib[i] = (fib[i - 2] + fib[i - 1]) % MOD

    i = 0
    ans = 1
    while i < N:
        c = S[i]
        if c == 'm' or c == 'w':
            return 0
        if c != 'u' and c != 'n':
            i += 1
            continue
        j = i
        while j < N and S[i] == S[j]:
            j += 1
        ans *= fib[j - i]
        ans %= MOD
        i = j

    return ans


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
