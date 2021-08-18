import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 998244353
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()


def resolve():
    N, K = LI()
    LR = [LI() for _ in range(K)]

    dp = [0] * N
    dp[0] = 1
    dp_acm = list(itertools.accumulate(dp, initial=0))
    for i in range(1, N):
        for l, r in LR:
            dp[i] += dp_acm[max(i - l + 1, 0)] - dp_acm[max(i - r, 0)]
            dp[i] %= MOD
        dp_acm[i + 1] = dp_acm[i] + dp[i]
        dp_acm[i + 1] %= MOD

    print((dp[-1]))


def __starting_point():
    resolve()


__starting_point()
