#!/usr/bin python3
# -*- coding: utf-8 -*-

# 双方向グラフで幅優先探索

from collections import deque

mod = 10**9+7

n, k = map(int, input().split())
graph = [[] for _ in range(n)]
#隣接リストの作成
for i in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    graph[a].append(b)
    graph[b].append(a)

#幅優先探索
q = deque()
seen = [False]*n
parent = [-1]*n
q.append(0)
seen[0] = True
parent[0] = 0
ret = k
while len(q)>0:
    cur = q.popleft()
    if cur == 0:
        cnt = k-1
    else:
        cnt = k-2
    for i in graph[cur]:
        if seen[i]==False:
            seen[i] = True
            #親
            parent[i] = cur
            q.append(i)
            ret *= cnt
            ret %= mod
            cnt -= 1
print(ret)
