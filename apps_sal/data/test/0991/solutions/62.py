import heapq
import sys
input = sys.stdin.readline


def dijkstra(edge, start):
    n = len(edge)
    dist = [float("inf")] * n
    dist[start] = 0
    que = [(0, start)]
    while que:
        d, v = heapq.heappop(que)
        if dist[v] < d:
            continue
        for nv, nd in edge[v]:
            if dist[nv] > d + nd:
                dist[nv] = d + nd
                heapq.heappush(que, (dist[nv], nv))
    return dist


n, m, s = map(int, input().split())
G = [[] for _ in range(n)]
if s >= 2500:
    for _ in range(m):
        u, v, a, b = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, b))
        G[v].append((u, b))
    L = dijkstra(G, 0)
else:
    for _ in range(m):
        u, v, a, b = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, a, b))
        G[v].append((u, a, b))
    CD = [list(map(int, input().split())) for _ in range(n)]
    edge = [[] for _ in range(n * 2500)]
    for i in range(n):
        c, d = CD[i]
        for k in range(2500):
            for v, a, b in G[i]:
                if k >= a:
                    edge[2500 * i + k].append((2500 * v + (k - a), b))
            if k + c < 2500:
                edge[2500 * i + k].append((2500 * i + (k + c), d))
    dist = dijkstra(edge, s)
    L = [0] * n
    for i in range(n):
        L[i] = min(dist[2500 * i:2500 * (i + 1)])
print(*L[1:], sep="\n")
