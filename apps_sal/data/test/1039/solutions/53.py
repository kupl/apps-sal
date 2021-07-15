#!/usr/bin python3
# -*- coding: utf-8 -*-

# ダイクストラ法
# 重み付きグラフ関係により最短経路のリストを作る
# 有向グラフで優先度付きキューで探索

from heapq import heapify, heappop, heappush, heappushpop

INF = float('inf')

def dijkstra(s,n,g):
    seen = [False]*n
    cost = [INF]*n
    cost[s] = 0 #スタートはコスト0
    next_q = [(0,s)]
    heapify(next_q)
    while len(next_q)>0:
        c, i = heappop(next_q)
        if cost[i] < c:
            continue
        for nedge, ncost in g[i]:
            nc = cost[i]+ncost
            if cost[nedge]>nc:
                cost[nedge] = nc
                heappush(next_q,(nc, nedge))
    return cost

def main():
    N = int(input())
    graph_F = [[] for _ in range(N)]
#    graph_R = [[] for _ in range(N)]
    #リストの作成
    for _ in range(N-1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph_F[a].append((b,c))
        graph_F[b].append((a,c))
#        graph_R[b].append((a,c))

    Q, K = map(int, input().split())
    K -= 1
    F = dijkstra(K,N,graph_F)
    for _ in range(Q):
        x, y = map(int, input().split())
        print(F[x-1]+F[y-1])

def __starting_point():
    main()
__starting_point()
