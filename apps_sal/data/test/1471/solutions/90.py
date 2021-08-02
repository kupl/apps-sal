def abc126_d():
    import sys
    sys.setrecursionlimit(10010010)
    read = sys.stdin.buffer.read
    inp = iter(map(int, read().split()))

    N = next(inp)
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u = next(inp) - 1
        v = next(inp) - 1
        w = next(inp)
        G[u].append((v, w))
        G[v].append((u, w))

    color = [-1] * N
    color[0] = 0

    def dfs(u):
        for v, w in G[u]:
            if color[v] != -1:
                continue
            if w % 2 == 0:
                color[v] = color[u]
            else:
                color[v] = abs(color[u] - 1)
            dfs(v)

    dfs(0)
    print(*color, sep='\n')


def __starting_point():
    abc126_d()


__starting_point()
