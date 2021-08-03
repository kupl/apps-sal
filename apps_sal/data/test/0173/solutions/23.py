def main():
    n, m = map(int, input().split())
    nm = n * m
    neigh = [[] for _ in range(nm)]
    for y, c in enumerate(input()):
        for x in range(y * m + 1, y * m + m):
            if c == '<':
                neigh[x].append(x - 1)
            else:
                neigh[x - 1].append(x)
    for x, c in enumerate(input()):
        for y in range(m + x, nm, m):
            if c == '^':
                neigh[y].append(y - m)
            else:
                neigh[y - m].append(y)

    def getdsu(t):
        if dsu[t] != t:
            dsu[t] = getdsu(dsu[t])
        return dsu[t]

    def setdsu(u, v):
        dsu[u] = getdsu(dsu[v])

    def dfs(yx):
        l[yx] = False
        for yx1 in neigh[yx]:
            if l[yx1]:
                setdsu(yx1, yx)
                dfs(yx1)

    for i in range(nm):
        l = [True] * nm
        dsu = list(range(nm))
        for j in range(i, i + nm):
            j %= nm
            if l[j]:
                dfs(j)
        if any(getdsu(_) != i for _ in range(nm)):
            print('NO')
            return
    print('YES')


def __starting_point():
    main()


__starting_point()
