def solve(n, p):
    i_p = list(enumerate(p))
    i_p.sort(key=lambda i_ab: (i_ab[1][1], i_ab[1][0], i_ab[0]))
    zig = list(reversed([i for (i, (a, b)) in i_p if a < b]))
    for i in range(len(zig) - 1):
        assert p[zig[i]][1] > p[zig[i + 1]][0]
    for i in zig:
        assert p[i][0] < p[i][1]
    zag = [i for (i, (a, b)) in i_p if a > b]
    for i in range(len(zag) - 1):
        assert p[zag[i]][1] < p[zag[i + 1]][0]
    for i in zag:
        assert p[i][0] > p[i][1]
    if len(zig) < len(zag):
        return zag
    return zig


def main():
    n = int(input())
    p = [None] * n
    for i in range(n):
        p[i] = tuple(map(int, input().split()))
    i = solve(n, p)
    print(len(i))
    print(*[ix + 1 for ix in i])


def __starting_point():
    main()


__starting_point()
