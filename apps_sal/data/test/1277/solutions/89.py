#!/usr/bin python3
# -*- coding: utf-8 -*-

# 双方向グラフで幅優先探索

from collections import deque

n, u, v = map(int, input().split())
g = [[] for _ in range(n)]
# 隣接リストの作成
for i in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)


# 幅優先探索
def bfs(x):
    q = deque()
    seen = [False] * n
    level = [-1] * n
    parent = [-1] * n
    q.append(x)
    seen[x] = True
    level[x] = 0
    parent[x] = 0
    while len(q) > 0:
        cur = q.popleft()
        lvl = level[cur]
        for i in g[cur]:
            if seen[i] == False:
                seen[i] = True
                # 階層
                level[i] = lvl + 1
                # 親
                parent[i] = cur
                q.append(i)
    return level


ul = bfs(u - 1)
vl = bfs(v - 1)

ret = 0
for i, j in zip(ul, vl):
    if i < j:
        ret = max(ret, j - 1)
print(ret)
