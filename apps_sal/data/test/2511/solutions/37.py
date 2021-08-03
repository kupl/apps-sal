#!/usr/bin python3
# -*- coding: utf-8 -*-

# 双方向グラフで幅優先探索
from collections import deque
mod = 10**9 + 7
N = 10**6                   # 出力の制限
g1 = [1] * (N + 1)              # 元テーブル
g2 = [1] * (N + 1)              # 逆元テーブル
for i in range(2, N + 1):  # 準備
    g1[i] = (g1[i - 1] * i) % mod
g2[N] = pow(g1[-1], mod - 2, mod)
for i in range(N, 0, -1):
    g2[i - 1] = (g2[i] * i) % mod


def nCr(n, r):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


def nPr(n, r):
    if (r < 0 or r > n):
        return 0
    return g1[n] * g2[n - r] % mod


n, k = map(int, input().split())
graph = [[] for _ in range(n)]
# 隣接リストの作成
for i in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)

# 幅優先探索
q = deque()
seen = [False] * n
parent = [-1] * n
q.append(0)
seen[0] = True
parent[0] = 0
ret = k
while len(q) > 0:
    cur = q.popleft()
    if cur == 0:
        cnt = k - 1
    else:
        cnt = k - 2
    for i in graph[cur]:
        if seen[i] == False:
            seen[i] = True
            # 親
            parent[i] = cur
            q.append(i)
            ret *= cnt
            ret %= mod
            cnt -= 1
print(ret)
