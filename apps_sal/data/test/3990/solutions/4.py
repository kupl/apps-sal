def main():
    n, m = list(map(int, input().split()))
    vrtxs = [[False] * n for _ in range(n)]
    for _ in range(m):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        vrtxs[u][v] = vrtxs[v][u] = True
    if vrtxs[0][n - 1]:
        for u, l in enumerate(vrtxs):
            for v, f in enumerate(l):
                l[v] = not f
            l[u] = False
    avail, nxt, t = [True] * n, [n - 1], 0
    while nxt:
        cur, nxt = nxt, []
        t += 1
        for u in cur:
            for v, f, a in zip(list(range(n)), vrtxs[u], avail):
                if f and a:
                    if not v:
                        print(t)
                        return
                    avail[v] = False
                    nxt.append(v)
    print(-1)


def __starting_point():
    main()

__starting_point()
