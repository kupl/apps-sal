import sys
from heapq import heappush, heappop

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *UVW = map(int, read().split())
    G = [[] for _ in range(N)]
    for u, v, w in zip(*[iter(UVW)] * 3):
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    dist = [INF] * N
    dist[0] = 0
    hq = [(0, 0)]

    while hq:
        d, v = heappop(hq)
        if d > dist[v]:
            continue
        for nv, cost in G[v]:
            if dist[nv] > dist[v] + cost:
                dist[nv] = dist[v] + cost
                heappush(hq, (dist[nv], nv))

    ans = [0] * N
    for i in range(N):
        ans[i] = 0 if dist[i] % 2 == 0 else 1

    print(*ans, sep='\n')
    return


def __starting_point():
    main()

__starting_point()
