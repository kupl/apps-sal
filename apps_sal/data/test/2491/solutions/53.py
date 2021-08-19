def Bellman_Ford(s, g, inf=1 << 60):
    N = len(g)
    dist = [inf] * N
    dist[s] = 0
    for _ in range(N):
        not_updated = True
        for v in range(N):
            for (u, c) in g[v]:
                if dist[v] == inf or dist[v] + c >= dist[u]:
                    continue
                dist[u] = dist[v] + c
                not_updated = False
        if not_updated:
            return -dist[N - 1]
    ret = dist[N - 1]
    for _ in range(N):
        not_updated = True
        for v in range(N):
            for (u, c) in g[v]:
                if dist[v] == inf or dist[v] + c >= dist[u]:
                    continue
                dist[u] = dist[v] + c
                not_updated = False
        if not_updated:
            break
    if ret == dist[N - 1]:
        return -ret
    else:
        return 'inf'


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    (N, M) = list(map(int, input().split()))
    g = tuple((set() for _ in range(N)))
    for _ in range(M):
        (a, b, c) = list(map(int, input().split()))
        a -= 1
        b -= 1
        g[a].add((b, -c))
    ans = Bellman_Ford(s=0, g=g)
    print(ans)


def __starting_point():
    main()


__starting_point()
