from itertools import permutations
import heapq


def dijkstra(N, G, s):
    INF = 10 ** 40
    d = [INF] * N
    d[s] = 0
    q = [(0, s)]
    while q:
        (c, v) = heapq.heappop(q)
        if d[v] < c:
            continue
        for (t, co) in G[v]:
            if d[v] + co < d[t]:
                d[t] = d[v] + co
                heapq.heappush(q, (d[t], t))
    return d


def main():
    (N, M, _) = list(map(int, input().split()))
    R = list(map(int, input().split()))
    R = [r - 1 for r in R]
    G = [[] for _ in range(N)]
    for _ in range(M):
        (a, b, c) = list(map(int, input().split()))
        G[a - 1].append((b - 1, c))
        G[b - 1].append((a - 1, c))
    RM = []
    for r in R:
        d = dijkstra(N, G, r)
        RM.append([d[rr] for rr in R])
    m = 10 ** 40
    for i in permutations(list(range(len(R)))):
        t = i[0]
        c = 0
        for r in i[1:]:
            c += RM[t][r]
            t = r
        m = min(m, c)
    return m


print(main())
