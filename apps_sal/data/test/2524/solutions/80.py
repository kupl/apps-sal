import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()


def resolve():
    N = I()
    A = LI()

    # 桁ごとに1の足される数を数える方針

    # 下準備 Aの中で、d桁目が1であるものの個数
    cnt = [0] * 60
    for i in A:
        for j in range(60):
            if i >> j & 1:
                cnt[j] += 1

    # 繰り上がりのない2進数→10進数に変換
    ans = 0
    for i in range(60):
        # i桁目に1の足される数に2のi乗をかければよい
        ans += cnt[i] * (N - cnt[i]) * pow(2, i, MOD)
        ans %= MOD

    print(ans)


def __starting_point():
    resolve()


__starting_point()
