def main():
    (n, m) = list(map(int, input().split()))
    l = [c for _ in range(n) for c in input()]
    neigh = []
    for y in range(n):
        for x in range(m):
            yx = y * m + x
            neigh.append([])
            if x and l[yx] == l[yx - 1]:
                neigh[-1].append(yx - 1)
                neigh[-2].append(yx)
            if y and l[yx] == l[yx - m]:
                neigh[-1].append(yx - m)
                neigh[-1 - m].append(yx)
    field = [0] * len(l)

    def dfs(t):
        field[t] = 1
        for v in neigh[t]:
            if not field[v]:
                neigh[v].remove(t)
                dfs(v)
            elif field[v] == 1:
                raise OverflowError
        field[t] = 2
    for (i, flag) in enumerate(field):
        if not flag:
            try:
                dfs(i)
            except OverflowError:
                print('Yes')
                return
    print('No')


def __starting_point():
    import sys
    sys.setrecursionlimit(10000)
    main()


__starting_point()
