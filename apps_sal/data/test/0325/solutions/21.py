def dfs(edge, s):
    use = {s}
    q = [s]
    while q:
        v = q.pop()
        for w in edge[v]:
            if w in use:
                continue
            use.add(w)
            q.append(w)
    return use


def bellman_ford(v, s, t, e):
    d = [10 ** 18] * v
    d[s] = 0
    for _ in range(v):
        f = False
        for (a, b, c) in e:
            cost = d[a] + c
            if cost < d[b]:
                d[b] = cost
                f = True
        if not f:
            break
    else:
        return -1
    return max(-d[t], 0)


def main():
    import sys
    input = sys.stdin.readline
    (n, m, p) = map(int, input().split())
    edge = [[] for _ in range(n)]
    edge_rev = [[] for _ in range(n)]
    e = []
    for _ in range(m):
        (a, b, c) = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge_rev[b - 1].append(a - 1)
        e.append((a - 1, b - 1, p - c))
    use = dfs(edge, 0) & dfs(edge_rev, n - 1)
    e = [(a, b, c) for (a, b, c) in e if a in use and b in use]
    print(bellman_ford(n, 0, n - 1, e))


def __starting_point():
    main()


__starting_point()
