def bfs(g, N, s, t):
    from collections import deque

    dist = [-1] * (N * 3)
    dist[s] = 0

    dq = deque()
    dq.append(s)

    while dq:
        v = dq.popleft()
        d = dist[v]
        for u in g[v]:
            if ~dist[u]:
                continue
            dist[u] = d + 1
            if u == t:
                return dist[t] // 3
            dq.append(u)
    return -1


def main():
    import sys
    input = sys.stdin.readline

    N, M = list(map(int, input().split()))

    g = tuple(set() for _ in range(N * 3))
    for _ in range(M):
        u, v = (int(x) - 1 for x in input().split())
        g[u].add(v + N)
        g[u + N].add(v + N * 2)
        g[u + N * 2].add(v)

    S, T = (int(x) - 1 for x in input().split())

    ans = bfs(g, N, S, T)

    print(ans)


def __starting_point():
    main()


__starting_point()
