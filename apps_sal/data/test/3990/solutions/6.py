def main():
    (n, m) = list(map(int, input().split()))
    vrtxs = [[] for _ in range(n)]
    for _ in range(m):
        (u, v) = list(map(int, input().split()))
        u -= 1
        v -= 1
        vrtxs[u].append(v)
        vrtxs[v].append(u)
    if n - 1 in vrtxs[0]:
        for (u, l) in enumerate(vrtxs):
            tmp = set(l)
            tmp.add(u)
            vrtxs[u] = [v for v in range(n) if v not in tmp]
    (avail, nxt, t) = ([True] * n, [n - 1], 0)
    while nxt:
        (cur, nxt) = (nxt, [])
        t += 1
        for u in cur:
            for v in vrtxs[u]:
                if avail[v]:
                    if not v:
                        print(t)
                        return
                    avail[v] = False
                    nxt.append(v)
    print(-1)


def __starting_point():
    main()


__starting_point()
