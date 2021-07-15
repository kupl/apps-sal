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
INF = float('inf')
MOD = 10 ** 9 + 7

N = INT()
S = input()

total = (N+1)*N // 2
ans = total - N

L = []
cnt = 1
for i in range(1, N):
    if S[i-1] == S[i]:
        cnt += 1
    else:
        L.append(cnt)
        cnt = 1
R = []
cnt = 1
for i in range(N-2, -1, -1):
    if S[i+1] == S[i]:
        cnt += 1
    else:
        R.append(cnt)
        cnt = 1

ans -= sum(L) + sum(R) - len(L)
print(ans)

