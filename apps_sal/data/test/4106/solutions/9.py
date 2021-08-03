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


INF = 10 ** 18
MOD = 10 ** 9 + 7

N, K, X = MAP()
A = [0] + LIST()

dp = list2d(X + 1, N + 1, -1)
dp[0][0] = 0
for i in range(X):
    for j in range(N):
        if dp[i][j] == -1:
            continue
        for k in range(j + 1, min(j + K + 1, N + 1)):
            dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + A[k])
ans = max(dp[X][-K:])
print(ans)
