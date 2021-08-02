def main():
    n = int(input())
    colors = input()[::2]
    edges = [[[] for _ in range(n)] for _ in (0, 1)]
    for _ in range(n - 1):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        e = edges[colors[u] != colors[v]]
        e[u].append(v)
        e[v].append(u)
    dsu, e = [-1] * n, edges[0]
    for u, v in enumerate(dsu):
        if v == -1:
            nxt, c = [u], colors[u]
            while nxt:
                cur, nxt = nxt, []
                for v in cur:
                    dsu[v] = u
                    for v in e[v]:
                        if dsu[v] == -1:
                            nxt.append(v)

    d = {u: [] for u, v in enumerate(dsu) if u == v}
    for u, e in enumerate(edges[1]):
        for v in e:
            d[dsu[u]].append(dsu[v])

    def bfs(x):
        nxt, visited, t = [x], set(), 0
        while nxt:
            t += 1
            cur, nxt = nxt, []
            for x in cur:
                visited.add(x)
                for y in d[x]:
                    if y not in visited:
                        nxt.append(y)
        return t, cur[0]

    print(bfs(bfs(0)[1])[0] // 2)


def __starting_point():
    main()


__starting_point()
