#!/usr/bin python3
# -*- coding: utf-8 -*-

# 双方向グラフで幅優先探索

from collections import deque

n, m = list(map(int, input().split()))
g = [set([]) for _ in range(n)]
# 隣接リストの作成
for i in range(m):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    g[a].add(b)

s, t = list(map(int, input().split()))
s, t = s - 1, t - 1

# 幅優先探索
q = deque()
level = [[-1] * n for i in range(3)]
q.append((s, 0))
level[0][s] = 0
while len(q) > 0:
    cur, lvl = q.popleft()
    nxtl = lvl + 1
    nxthp = nxtl % 3
    for i in g[cur]:
        if level[nxthp][i] == -1:
            # 階層
            level[nxthp][i] = nxtl
            q.append((i, nxtl))
print((level[0][t] // 3))
