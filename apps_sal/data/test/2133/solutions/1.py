def main():
    n = int(input())
    colors = [c == '1' for c in input()[::2]]
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
                dsu[b] = u
                while v != a:
                    u = dsu[v]
                    dsu[v] = a
                    v = u
            else:
                dsu[a] = v
                while u != b:
                    v = dsu[u]
                    dsu[u] = b
                    u = v
        else:
            edges[u].append(v)
            edges[v].append(u)
    for u, v in enumerate(dsu):
        dsu[u] = dsu[v]
    if not any(dsu):
        print(0)
        return
    d = {u: set() for u, v in enumerate(dsu) if u == v}
    for u, e in enumerate(edges):
        u = dsu[u]
        for v in e:
            v = dsu[v]
            d[u].add(v)
            d[v].add(v)

    def bfs(x):
        nxt, visited, t = [x], set(), 0
        while nxt:
            t += 1
            cur, nxt = nxt, []
            for u in cur:
                visited.add(u)
                for v in d[u]:
                    if v not in visited:
                        nxt.append(v)
        return t, cur[0]

    print(bfs(bfs(0)[1])[0] // 2)


def __starting_point():
    main()


__starting_point()
