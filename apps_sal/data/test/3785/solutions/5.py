def main():
    (n, m, k) = map(int, input().split())
    mn = m * n
    l = [_ == '.' for _ in range(n) for _ in input()]
    neigh = [[] for _ in range(mn)]
    for y in range(n - 1):
        for x in range(m):
            yx = y * m + x
            if l[yx] and l[yx + m]:
                neigh[yx].append(yx + m)
                neigh[yx + m].append(yx)
    for y in range(n):
        for x in range(m - 1):
            yx = y * m + x
            if l[yx] and l[yx + 1]:
                neigh[yx].append(yx + 1)
                neigh[yx + 1].append(yx)
    res = [True] * mn
    nxt = {l.index(True)}
    cnt = sum(l) - k
    while cnt:
        (cur, nxt) = (nxt, set())
        for i in cur:
            if res[i]:
                res[i] = False
                cnt -= 1
                if not cnt:
                    break
                for j in neigh[i]:
                    nxt.add(j)
    for (x, (a, b)) in enumerate(zip(res, l)):
        if a and b:
            l[x] = 2
    l = [''.join((('#', '.', 'X')[_] for _ in l[x:x + m])) for x in range(0, mn, m)]
    print('\n'.join(l))


def __starting_point():
    main()


__starting_point()
