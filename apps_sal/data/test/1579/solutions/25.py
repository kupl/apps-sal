def main():
    from collections import Counter
    import sys
    input = sys.stdin.readline
    MX = 10 ** 5 + 10
    (*p,) = [r for r in range(MX * 2)]

    def root(x):
        if x == p[x]:
            return x
        p[x] = y = root(p[x])
        return y

    def unite(x, y):
        px = root(x)
        py = root(y)
        if px == py:
            return 0
        if px < py:
            p[py] = px
        else:
            p[px] = py
        return 1
    n = int(input())
    for _ in range(n):
        (x, y) = (int(x) - 1 for x in input().split())
        unite(x, y + MX)
    ctr_x = Counter((root(r) for r in range(MX)))
    ctr_y = Counter((root(r) for r in range(MX, MX * 2)))
    rs = set(ctr_x.keys())
    rs.update(list(ctr_y.keys()))
    ans = sum((ctr_x[r] * ctr_y[r] for r in rs)) - n
    print(ans)


def __starting_point():
    main()


__starting_point()
