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
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 18
MOD = 10 ** 9 + 7

S = input()
N = len(S)

dp = [0] * (N+1)
dp[0] = 1
for i in range(N):
    if S[i] == 'w' or S[i] == 'm':
        print(0)
        return
    dp[i+1] += dp[i]
    dp[i+1] %= MOD
    if i+2 <= N:
        if S[i] == S[i+1] == 'u' \
                or S[i] == S[i+1] == 'n':
            dp[i+2] += dp[i]
            dp[i+2] %= MOD
print(dp[N])

