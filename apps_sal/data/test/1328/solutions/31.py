def half_enumeration(a, *, func):
    """正しい英訳は不明"""
    n = len(a)
    h = n // 2

    def enum(h, *, second_half: bool = False) -> set:
        p = set()
        if second_half:
            b = a[h:]
        else:
            b = a[:h]

        for x in b:
            q = set()
            for e in p:
                q.add(func(e, x))
            p.add(x)
            p.update(q)
        return p

    return enum(h), enum(h, second_half=True)


def main():
    INF = 40 * 100 + 1

    N, Ma, Mb = list(map(int, input().split()))

    def update(e, x):
        return e[0] + x[0], e[1] + x[1]

    xcs = []
    for _ in range(N):
        ai, bi, ci = list(map(int, input().split()))
        x = Ma * bi - Mb * ai  # Σai:Σbi=Ma:Mb<->Ma*Σbi-Mb*Σai=0
        xcs.append((x, ci))

    p1, p2 = half_enumeration(xcs, func=update)

    t1 = [INF] * (INF * 2 + 1)
    t2 = [INF] * (INF * 2 + 1)
    for x, c in p1:
        t1[x] = min(t1[x], c)
    for x, c in p2:
        t2[x] = min(t2[x], c)

    ans = min(t1[0], t2[0])
    for x in range(-INF, INF + 1):
        ans = min(ans, t1[x] + t2[-x])

    print((-1 if ans == INF else ans))


def __starting_point():
    main()

__starting_point()
