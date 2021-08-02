def abc126_e():
    n, m = map(int, input().split())
    par = [x for x in range(n)]
    rank = [0] * n

    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]

    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y: return
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]: rank[x] += 1

    for _ in range(m):
        x, y, z = map(int, input().split())
        unite(x - 1, y - 1)

    for i in range(n):
        _ = find(i)

    ans = len(set(par))
    print(ans)


def __starting_point():
    abc126_e()


__starting_point()
