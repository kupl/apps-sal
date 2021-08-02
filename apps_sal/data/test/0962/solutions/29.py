# -*- coding: utf-8 -*-

import sys


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7


def SCC(N, edges):
    """ 強連結成分分解 """

    nodes1 = [[] for i in range(N)]
    nodes2 = [[] for i in range(N)]
    for u, v in edges:
        nodes1[u].append(v)
        nodes2[v].append(u)

    T = []
    visited = [False] * N

    def rec1(cur):
        visited[cur] = True
        for nxt in nodes1[cur]:
            if not visited[nxt]:
                rec1(nxt)
        # 行き止まったところから順にTに入れていく
        T.append(cur)

    # グラフが連結とは限らないので全頂点やる
    for u in range(N):
        if not visited[u]:
            rec1(u)

    visited = [False] * N
    group = [0] * N
    grpcnt = 0

    def rec2(cur):
        group[cur] = grpcnt
        visited[cur] = True
        for nxt in nodes2[cur]:
            if not visited[nxt]:
                rec2(nxt)

    # 逆順で進めるところまで行く
    for u in reversed(T):
        if not visited[u]:
            rec2(u)
            grpcnt += 1
    return grpcnt, group


def bfs(N, nodes, src):
    """ BFS(一般グラフ、重みなし) """
    from collections import deque

    que = deque([(src, -1, 0)])
    dist = [()] * N
    mn = INF
    end = -1
    while que:
        u, prev, c = que.popleft()
        # 同じ強連結成分内のみでやる
        if group[u] != group[src]:
            continue
        if dist[u]:
            # 訪問済で始点に帰ってきたら、最短チェック
            if u == src:
                if c < mn:
                    mn = c
                    end = prev
            continue
        dist[u] = (c, prev)
        for v in nodes[u]:
            que.append((v, u, c + 1))
    # 経路、始点に戻ってくる最短距離、その直前の頂点を返す
    return dist, mn, end


def get_route(s, t, res):
    """ s,t間の経路を取得 """
    prev = t
    StoT = [t]
    while prev != s:
        prev = res[prev][1]
        if prev == -1:
            return None
        StoT.append(prev)
    StoT = StoT[::-1]
    return StoT


N, M = MAP()
nodes = [[] for i in range(N)]
edges = []
for i in range(M):
    a, b = MAP()
    a -= 1
    b -= 1
    nodes[a].append(b)
    edges.append((a, b))

# 強連結成分毎に見る
grpcnt, group = SCC(N, edges)
ans = INF
for i in range(N):
    # 経路、始点に戻ってくる最短距離、その直前の頂点
    dist, mn, end = bfs(N, nodes, i)
    if mn < ans:
        ans = mn
        route = get_route(i, end, dist)
if ans != INF:
    print(ans)
    [print(u + 1) for u in route]
else:
    # そもそも閉路なし
    print(-1)
