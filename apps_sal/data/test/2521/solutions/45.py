# -*- coding: utf-8 -*-

import sys
from heapq import heapify, heappush, heappop


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
A = LIST()

A1 = A[:N]
A2 = A[N:N * 2]
A3 = [-a for a in A[N * 2:]]
heapify(A1)
heapify(A3)

# 真ん中グループ(A2)をiまで左に取り込んだ時の左グループ(A1)の最大値
ansa = [0] * (N + 1)
ansa[0] = sum(A1)
for i in range(N):
    heappush(A1, A2[i])
    ansa[i + 1] = ansa[i] + A2[i] - heappop(A1)

# 真ん中グループ(A2)を後ろからiまで右に取り込んだ時の右グループ(A1)の最小値
ansb = [0] * (N + 1)
ansb[N] = -sum(A3)
for i in range(N - 1, -1, -1):
    heappush(A3, -A2[i])
    ansb[i] = ansb[i + 1] + A2[i] - (-heappop(A3))

# 各位置iから一番いい場所を得る
ans = -INF
for i in range(N + 1):
    ans = max(ans, ansa[i] - ansb[i])
print(ans)
