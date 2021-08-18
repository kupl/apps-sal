
from heapq import heappop, heappush

icase = 0
if icase == 0:
    n = int(input())
    g = [[] for i in range(n)]
    for i in range(n - 1):
        ai, bi, ci = list(map(int, input().split()))
        g[ai - 1].append((bi - 1, ci))
        g[bi - 1].append((ai - 1, ci))
if icase == 1:
    n = 5
    g = [[(1, 1), (2, 1)], [(0, 1), (3, 1)], [(0, 1), (4, 1)], [(1, 1)], [(2, 1)]]
if icase == 2:
    n = 7
    g = [[(1, 1), (2, 3), (3, 5), (4, 7), (5, 9), (6, 11)], [(0, 1)], [(0, 3)], [(0, 5)], [(0, 7)], [(0, 9)], [(0, 11)]]

q, k = list(map(int, input().split()))
k = k - 1

hq = []
heappush(hq, (0, k))

inf = float("INF")
dist = [inf] * n
dist[k] = 0
while len(hq) > 0:
    dd, state = heappop(hq)
    for v, dv in g[state]:
        if dist[v] > dist[state] + dv:
            dist[v] = dist[state] + dv
            heappush(hq, (dist[v], v))

for i in range(q):
    xi, yi = list(map(int, input().split()))
    print((dist[xi - 1] + dist[yi - 1]))
