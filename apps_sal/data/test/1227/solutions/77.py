import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()


def resolve():
    N = I()
    K = I()

    # [0, N]で、non0の数字がK個あるものの数
    @functools.lru_cache
    def f(N, K):
        if N == K == 0:
            ret = 1
        elif N > 0 and K >= 0:
            ret = f(N // 10, K) + N % 10 * f(N // 10, K - 1) + (9 - N % 10) * f(N // 10 - 1, K - 1)
        else:
            ret = 0
        return ret

    ans = f(N, K)
    print(ans)


def __starting_point():
    resolve()


__starting_point()
