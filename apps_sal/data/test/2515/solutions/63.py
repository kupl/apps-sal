import sys
import math
from functools import lru_cache
import numpy as np
from collections import defaultdict
sys.setrecursionlimit(10**9)
MOD = 10**9 + 7


def input():
    return sys.stdin.readline()[:-1]


def mi():
    return list(map(int, input().split()))


def ii():
    return int(input())


def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

# nまでの自然数が素数かどうかを表すリストを返す


def makePrimeChecker(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    return isPrime


def main():
    Q = ii()
    l, r = i2(Q)
    m = max(r)

    dp = [0] * (m + 1)
    check = makePrimeChecker(m)

    for i in range(1, m + 1):
        if check[i] and check[(i + 1) // 2]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]

    for ll, rr in zip(l, r):
        print((dp[rr] - dp[ll - 1]))


def __starting_point():
    main()


__starting_point()
