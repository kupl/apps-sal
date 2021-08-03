def main():
    d, m = {}, 0
    for i in range(1, int(input()) + 1):
        a, b, c = sorted(map(int, input().split()))
        if (b, c) in d:
            x, y, z, t = d[b, c]
            if a > z:
                d[b, c] = (a, i, x, y) if a > x else (x, y, a, i)
        else:
            d[b, c] = (a, i, 0, 0)
    for (a, b), (x, y, z, t) in list(d.items()):
        if a > m < x + z:
            m, res = x + z if a > x + z else a, (y, t)
    print(("2\n%d %d" % res) if res[1] else ("1\n%d" % res[0]))


def __starting_point():
    main()


__starting_point()
