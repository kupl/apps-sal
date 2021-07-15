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

N, K, Q = MAP()
A = LIST()

ans = INF
# 使う要素の最小値とする値xを全探索
for x in A:
    # 数列Aをx未満の値で区切った数列Bを作る
    B = []
    tmp = []
    for i in range(N):
        if A[i] >= x:
            tmp.append(A[i])
        else:
            B.append(tmp)
            tmp = []
    B.append(tmp)
    # 数列B内の各数列から、使える要素を集める
    C =  []
    for li in B:
        m = len(li)
        if m-K+1 >= 1:
            li.sort()
            C += li[:m-K+1]
    # 集めた要素からQ個をクエリで使うので、小さい方からQ番目が使う要素の最大値y
    C.sort()
    if len(C) < Q:
        continue
    y = C[Q-1]
    ans = min(ans, y - x)
print(ans)

