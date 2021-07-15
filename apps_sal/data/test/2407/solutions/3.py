3

import array
import math
import os
import sys


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, R, X):
    v = list(set(X))
    v.sort(reverse=True)
    off = 0
    c = 0
    i = 0
    while i < len(v):
        x = v[i]
        if x <= off:
            break
        i += 1
        c += 1
        off += R

    return c


def main():
    Q = int(inp())
    for _ in range(Q):
        N, R = [int(e) for e in inp().split()]
        X = [int(e) for e in inp().split()]
        print(solve(N, R, X))


def __starting_point():
    main()

__starting_point()
