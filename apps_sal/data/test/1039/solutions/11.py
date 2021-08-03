def abc070_d():
    import sys
    sys.setrecursionlimit(10010010)
    read = sys.stdin.buffer.read
    inp = iter(map(int, read().split()))

    n = next(inp)
    adjlist = [[] for _ in range(n)]
    for _ in range(n - 1):
        a = next(inp) - 1
        b = next(inp) - 1
        c = next(inp)
        adjlist[a].append((b, c))
        adjlist[b].append((a, c))

    q = next(inp)
    k = next(inp) - 1

    dist = [-1] * n

    def dfs(x: int, d: int):
        dist[x] = d
        for nx, nd in adjlist[x]:
            if dist[nx] != -1:
                continue
            dfs(nx, d + nd)

    dfs(k, 0)

    for _ in range(q):
        x = next(inp) - 1
        y = next(inp) - 1
        ans = dist[x] + dist[y]
        print(ans)


def __starting_point():
    abc070_d()


__starting_point()
