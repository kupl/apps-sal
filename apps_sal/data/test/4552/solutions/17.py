import sys, math
from functools import lru_cache
from collections import defaultdict
from decimal import Decimal
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return list(map(int, input().split()))

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N = ii()
    F = [list(mi()) for i in range(N)]
    P = [list(mi()) for i in range(N)]

    m = -math.inf

    for ptn in range(1, 2**10):
        r = 0
        for i in range(N):
            cnt = 0
            for j in range(10):
                if F[i][j] and (ptn>>j)&1:
                    cnt += 1
            r += P[i][cnt]
        m = max(m, r)

    print(m)


def __starting_point():
    main()

__starting_point()
