def main():
    n, m = list(map(int, input().split()))
    edges = {_: {} for _ in range(1, m + 1)}
    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        d = edges[c]
        l = d.get(a)
        if l:
            l.append(b)
        else:
            d[a] = [b]
        l = d.get(b)
        if l:
            l.append(a)
        else:
            d[b] = [a]

    def dfs(t):
        unused[t] = False
        for y in dcolor.get(t, ()):
            if unused[y]:
                dfs(y)

    res = []
    n += 1
    unused = [True] * n
    for _ in range(int(input())):
        a, b = list(map(int, input().split()))
        x = 0
        for dcolor in list(edges.values()):
            for j in range(n):
                unused[j] = True
            dfs(a)
            if not unused[b]:
                x += 1
        res.append(str(x))
    print('\n'.join(res))


def __starting_point():
    main()


__starting_point()
