def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    N, M = list(map(int, input().split()))

    g = tuple(set() for _ in range(N * 3))
    for _ in range(M):
        u, v = (int(x) - 1 for x in input().split())
        g[u].add(v + N)
        g[u + N].add(v + N + N)
        g[u + N + N].add(v)

    S, T = (int(x) - 1 for x in input().split())

    dist = [-1] * (N * 3)
    dist[S] = 0

    dq = deque()
    dq.append(S)
    while dq:
        v = dq.popleft()
        for u in g[v]:
            if ~dist[u]: continue
            dist[u] = dist[v] + 1
            dq.append(u)

    if dist[T] % 3:
        print((-1))
        return

    print((dist[T] // 3))


def __starting_point():
    main()

__starting_point()
