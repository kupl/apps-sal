3

import os
import sys


def main():
    T = read_int()
    for _ in range(T):
        N = read_int()
        A = read_ints()
        print(solve(N, A))


def solve(N, A):
    if N <= 1:
        return -1
    INF = N + 1
    best = INF
    pos = {}
    for i, a in enumerate(A):
        if a in pos:
            best = min(best, i - pos[a] + 1)
        pos[a] = i
    if best == INF:
        return -1
    return best


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
