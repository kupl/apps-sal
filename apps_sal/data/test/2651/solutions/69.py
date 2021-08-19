# -*- coding: utf-8 -*-

import sys


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

N, M = MAP()
A = LIST()
B = LIST()

# 縦横独立に、全区間総和を取る
lsm = rsm = 0
for i in range(N):
    lsm += A[i] * (N - i - 1)
    rsm += A[i] * i
    lsm %= MOD
    rsm %= MOD
h = rsm - lsm
lsm = rsm = 0
for i in range(M):
    lsm += B[i] * (M - i - 1)
    rsm += B[i] * i
    lsm %= MOD
    rsm %= MOD
w = rsm - lsm

ans = h * w % MOD
print(ans)
