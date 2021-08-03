def main():
    n = int(input())
    colors = input()[::2]
    dsu = list(range(n))
    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        if colors[u] == colors[v]:
            a, b = dsu[u], dsu[v]
            while a != dsu[a]:
                a = dsu[a]
            while b != dsu[b]:
                b = dsu[b]
            if a < b:
                dsu[b] = dsu[v] = a
            else:
                dsu[a] = dsu[u] = b
        else:
            edges[u].append(v)
    for u, v in enumerate(dsu):
        dsu[u] = dsu[v]
    d = {u: [] for u, v in enumerate(dsu) if u == v}
    for u, e in enumerate(edges):
        for v in e:
            d[dsu[u]].append(dsu[v])
            d[dsu[v]].append(dsu[u])

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
