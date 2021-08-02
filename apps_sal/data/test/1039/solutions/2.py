import sys
from collections import defaultdict
from heapq import heappush, heappop


def input():
    return sys.stdin.readline().strip()


def dijkstra(adj_list, start):
    n = len(adj_list)
    dist = [float("inf")] * n
    dist[start] = 0

    pq = []
    heappush(pq, (0, start))
    visited = set()
    while pq:
        w, v = heappop(pq)
        if dist[v] < w:
            continue
        visited.add(v)
        for nv, nw in adj_list[v]:
            if nv in visited:
                continue
            if dist[nv] > dist[v] + nw:
                dist[nv] = dist[v] + nw
                heappush(pq, (dist[nv], nv))
    return dist


N = int(input())
g = defaultdict(list)
for _ in range(N - 1):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))
Q, K = list(map(int, input().split()))
K -= 1
d = dijkstra(g, K)
ans = []
for _ in range(Q):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    print((d[x] + d[y]))
