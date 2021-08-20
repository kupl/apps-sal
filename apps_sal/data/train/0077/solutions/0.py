import sys
import os
import math
3
DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


INF = 10 ** 20


def solve(N, A, B):
    dp = {A[0]: 0, A[0] + 1: B[0], A[0] + 2: B[0] * 2}
    for i in range(1, N):
        ndp = {}
        h = A[i]
        for (ph, c) in dp.items():
            for inc in range(3):
                nh = h + inc
                if ph == nh:
                    continue
                if nh not in ndp:
                    ndp[nh] = INF
                ndp[nh] = min(ndp[nh], c + B[i] * inc)
        dp = ndp
    return min(dp.values())


def main():
    Q = int(inp())
    for _ in range(Q):
        N = int(inp())
        A = []
        B = []
        for _ in range(N):
            (a, b) = [int(e) for e in inp().split()]
            A.append(a)
            B.append(b)
        print(solve(N, A, B))


def __starting_point():
    main()


__starting_point()
