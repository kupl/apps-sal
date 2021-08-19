#!/usr/bin python3
# -*- coding: utf-8 -*-

# ワーシャルフロイド法
# 全頂点間最短路
# d[i][j]は2頂点間i, j間の移動コストを格納, Mは頂点数

import copy
INF = float("inf")


def warshall_floyd(d):
    n = len(d)
    wf = copy.deepcopy(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                wf[i][j] = min(wf[i][j], wf[i][k] + wf[k][j])
    return wf  # d[i][j]に頂点i, j間の最短距離を格納

##############################


n, m = list(map(int, input().split()))  # N:頂点数 m:辺の数
d = [[INF] * n for i in range(n)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
edges = []
for i in range(m):
    u, v, w = list(map(int, input().split()))
    d[u - 1][v - 1] = w
    d[v - 1][u - 1] = w
    edges.append((u - 1, v - 1))
for i in range(n):
    d[i][i] = 0  # 自身のところに行くコストは０

fwd = warshall_floyd(d)  # d[i][j]に頂点i, j間の最短距離を格納

ret = 0
for u, v in edges:
    if fwd[u][v] < d[u][v]:
        ret += 1
print(ret)
