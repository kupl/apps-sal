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
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()


def combMod(n, r, p):
    numer = 1
    denom = 1
    for i in range(1, r + 1):
        numer = numer * (n - r + i) % p
        denom = denom * i % p
    return numer * pow(denom, p - 2, p) % p


def resolve():
    N, K = LI()

    for i in range(1, K + 1):
        if i <= N - K + 1:
            ans = combMod(K - 1, i - 1, MOD) * combMod(N - K + 1, i, MOD) % MOD
            print(ans)
        else:
            print((0))


def __starting_point():
    resolve()


__starting_point()
