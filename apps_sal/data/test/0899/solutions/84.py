import sys
from heapq import heappush, heappop

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *AB = list(map(int, read().split()))
    G = [[] for _ in range(N)]
    for i, (a, b, c) in enumerate(zip(*[iter(AB)] * 3)):
        G[a - 1].append((b - 1, c, i))
        G[b - 1].append((a - 1, c, i))

    vec = [False] * M
    for i in range(N):
        dist = [INF] * N
        dist[i] = 0
        from_edge = [[] for _ in range(N)]
        hq = [(0, i)]

        while hq:
            d, v = heappop(hq)
            if dist[v] < d:
                continue
            for nv, cost, edge in G[v]:
                if dist[nv] > d + cost:
                    dist[nv] = d + cost
                    heappush(hq, (dist[nv], nv))
                    from_edge[nv] = [edge]
                elif dist[nv] == d + cost:
                    from_edge[nv].append(edge)

        for edges in from_edge:
            for e in edges:
                vec[e] = True

    ans = sum(1 for flag in vec if not flag)
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
