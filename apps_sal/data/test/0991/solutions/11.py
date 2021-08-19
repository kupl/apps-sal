import sys
import heapq


def dijkstra(s, es):
    INF = sys.maxsize
    cs = [INF] * len(es)
    (cs[s], hq) = (0, [])
    heapq.heapify(hq)
    heapq.heappush(hq, (cs[s], s))
    while hq:
        (d, v) = heapq.heappop(hq)
        if cs[v] < d:
            continue
        for (t, b) in es[v]:
            if cs[t] > cs[v] + b:
                cs[t] = cs[v] + b
                heapq.heappush(hq, (cs[t], t))
    return cs


def nwc(n, c):
    MAX_COINS = 2500
    return (MAX_COINS + 1) * n + c


def main():
    MAX_COINS = 2500
    (N, M, S) = tuple(map(int, sys.stdin.readline().split()))
    S = S if S < MAX_COINS else MAX_COINS
    es = [[] for _ in range(N * (MAX_COINS + 1))]
    for _ in range(M):
        (u, v, a, b) = tuple(map(int, sys.stdin.readline().split()))
        (u, v) = (u - 1, v - 1)
        for c in range(a, MAX_COINS + 1):
            es[nwc(u, c)].append((nwc(v, c - a), b))
            es[nwc(v, c)].append((nwc(u, c - a), b))
    for n in range(N):
        (c, d) = tuple(map(int, sys.stdin.readline().split()))
        c = c if c < MAX_COINS else MAX_COINS
        for i in range(0, MAX_COINS - c + 1):
            es[nwc(n, i)].append((nwc(n, i + c), d))
    cs = dijkstra(nwc(0, S), es)
    for n in range(1, N):
        print(min(cs[n * (MAX_COINS + 1):(n + 1) * (MAX_COINS + 1)]))


def __starting_point():
    main()


__starting_point()
