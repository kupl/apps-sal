import sys
from heapq import heapify, heappop, heappush


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N, M = lr()
graph = [[] for _ in range((N + 1) * 3)]
for _ in range(M):
    a, b = lr()
    a *= 3
    b *= 3
    for i in range(3):
        j = i + 1 if i < 2 else 0
        graph[a + i].append(b + j)

INF = 10 ** 15


def dijkstra(start):
    dist = [INF] * (N + 1) * 3
    dist[start] = 0
    que = [(0, start)]
    while que:
        d, prev = heappop(que)
        if dist[prev] < d:
            continue
        for next in graph[prev]:
            d1 = d + 1
            if dist[next] > d1:
                dist[next] = d1
                heappush(que, (d1, next))
    return dist


S, T = lr()
dist = dijkstra(S * 3)
answer = dist[T * 3]
if answer == INF:
    answer = -1
else:
    answer //= 3
print(answer)
