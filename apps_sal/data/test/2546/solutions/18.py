3

import array
import math
import os
import sys


def main():
    T = read_int()
    for _ in range(T):
        N, S = read_ints()
        A = [read_ints() for _ in range(N)]
        print(solve(N, S, A))


def solve(N, S, A):
    minv = [l for l, r in A]
    minv.sort()

    half = N // 2

    def feasible(target):
        low = []
        high = []
        mid = []
        for p in A:
            l, r = p
            if target < l:
                high.append(p)
            elif r < target:
                low.append(p)
            else:
                mid.append(p)

        if len(low) >= half + 1 or len(high) >= half + 1:
            return False

        tsum = 0
        for l, r in low:
            tsum += l
        for l, r in high:
            tsum += l

        mid.sort()
        midi = half - len(low)
        for i in range(midi):
            l, r = mid[i]
            tsum += l
        tsum += target * (len(mid) - midi)

        return tsum <= S

    lb = minv[half]
    ub = 10 ** 9 + 1
    while ub - lb > 1:
        mid = (ub + lb) // 2
        if feasible(mid):
            lb = mid
        else:
            ub = mid
    return lb


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
