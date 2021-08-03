def main():
    from collections import defaultdict
    n, colors = int(input()), input()[::2]
    dsu, edges, d = list(range(n)), [], defaultdict(list)
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
            edges.append(u)
            edges.append(v)
    for u, v in enumerate(dsu):
        dsu[u] = dsu[v]
    while edges:
        u, v = dsu[edges.pop()], dsu[edges.pop()]
        d[u].append(v)
        d[v].append(u)

    def bfs(x):
        nxt, avail, t = [x], [True] * n, 0
        while nxt:
            t += 1
            cur, nxt = nxt, []
            for y in cur:
                avail[y] = False
                for y in d[y]:
                    if avail[y]:
                        nxt.append(y)
        return t if x else cur[0]

    print(bfs(bfs(0)) // 2)


def __starting_point():
    main()


__starting_point()
