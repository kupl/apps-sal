
def main():
    import sys
    input = sys.stdin.readline

    MX = 10 ** 5 + 10

    *p, = [r for r in range(MX * 2)]

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
        x, y = (int(x) - 1 for x in input().split())
        unite(x, y + MX)

    xs = [0] * (MX * 2)
    ys = [0] * (MX * 2)

    for r in range(MX):
        xs[root(r)] += 1

    for r in range(MX, MX * 2):
        ys[root(r)] += 1

    ans = -n
    for r in range(MX * 2):
        ans += xs[r] * ys[r]

    print(ans)


def __starting_point():
    main()


__starting_point()
