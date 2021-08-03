def bellman(s, n, es):
    INF = float("inf")
    d = [INF] * n
    d[s] = 0
    for _ in range(n - 1):
        for p, q, r in es:
            if d[p] != INF and d[q] > d[p] + r:
                d[q] = d[p] + r

    for _ in range(n - 1):
        for p, q, r in es:
            if d[q] > d[p] + r:
                d[q] = -INF
    return d


n, m = map(int, input().split())
g = []
for _ in range(m):
    vi, vj, w = map(int, input().split())
    g.append([vi - 1, vj - 1, -w])
print(-bellman(0, n, g)[-1])
