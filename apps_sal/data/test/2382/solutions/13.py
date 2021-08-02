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

N = INT()
A = LIST()

A.sort(reverse=1)
cur = [A[0]]
# 作成済を-1とする
A[0] = -1

for _ in range(N):
    cur.sort(reverse=1)
    nxt = cur[:]
    j = 0
    for i, a in enumerate(A):
        if a == -1:
            continue
        if a < cur[j]:
            # 大きい要素から順に、まだ作っていない大きい要素を作っていく
            nxt.append(a)
            A[i] = -1
            j += 1
            # この世代は作り終わった
            if j == len(cur):
                break
    else:
        # 子要素を作れない要素があった
        No()
        return
    cur = nxt[:]
Yes()
