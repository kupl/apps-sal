
"""
01-BFS
辺の重みが0 or 1 のとき、dequeを使ってdijkstraを高速化できる
"""
import sys
from collections import deque


def bfs01(g, start):
    n = len(g)
    res = [float("inf")] * n
    res[start] = 0
    pending = n - 1
    q = deque([(0, start)])
    while q and pending:
        dv, v = q.popleft()
        if res[v] < dv:
            continue
        pending -= 1
        for to, cost in g[v]:
            if dv + cost < res[to]:
                res[to] = dv + cost
                if cost:
                    q.append((res[to], to))
                else:
                    q.appendleft((res[to], to))
    return res


sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

k = int(input())

g = [[] for _ in range(k)]
for i in range(k):
    g[i].append(((i + 1) % k, 1))
    g[i].append((10 * i % k, 0))

res = bfs01(g, 1)
print((res[0] + 1))
