
from heapq import heappush, heappop


def resolve():
    INF = 1 << 60
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, c = [int(x) - 1 for x in input().split()]
        G[a].append((b, c + 1))
        G[b].append((a, c + 1))

    Q, K = list(map(int, input().split()))

    K -= 1
    dist = [INF] * N
    hq = []
    heappush(hq, (K, 0))
    dist[K] = 0
    while hq:
        v, cost = heappop(hq)
        for to, c in G[v]:
            if dist[to] <= dist[v] + c:
                continue
            dist[to] = dist[v] + c
            heappush(hq, (to, dist[to]))

    for _ in range(Q):
        x, y = [int(x) - 1 for x in input().split()]
        print((dist[x] + dist[y]))


def __starting_point():
    resolve()


__starting_point()
