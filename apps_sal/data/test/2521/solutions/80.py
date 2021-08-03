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
INF = 10 ** 18
MOD = 10 ** 9 + 7

N = INT()
A = LIST()

A1 = A[:N]
A2 = A[N:]
sm1 = sum(A1)
sm2 = sum(A2)
que1 = []
que2 = []
S = set()
for i, a in enumerate(A1):
    que1.append((a, i))
heapify(que1)
A2 = [(a, i) for i, a in enumerate(A2, N)]
A2.sort(reverse=1)
for a, i in A2[:N]:
    sm2 -= a
    S.add(i)
    que2.append((a, i))
heapify(que2)

ans = sm1 - sm2
for i in range(N, N * 2):
    # 前半
    heappush(que1, (A[i], i))
    sm1 += A[i]
    a, _ = heappop(que1)
    sm1 -= a
    # 後半
    if i not in S:
        sm2 -= A[i]
        while 1:
            a, j = heappop(que2)
            S.remove(j)
            if j > i:
                sm2 += a
                break
    ans = max(ans, sm1 - sm2)
print(ans)
