def main():
    from math import hypot
    from sys import stdin
    ax, ay, bx, by, tx, ty = list(map(float, input().split()))
    s, tot = input(), 0.
    m0 = m1 = m2 = m3 = -9e9
    j = k = 0
    for i, s in enumerate(stdin.read().splitlines()):
        x, y = list(map(float, s.split()))
        r = hypot(tx - x, ty - y)
        tot += r
        d = r - hypot(ax - x, ay - y)
        if m1 < d:
            if m0 < d:
                m0, m1, j = d, m0, i
            else:
                m1 = d
        d = r - hypot(bx - x, by - y)
        if m3 < d:
            if m2 < d:
                m2, m3, k = d, m2, i
            else:
                m3 = d
    print(tot * 2. - max((m0, m2, m0 + m2) if j != k else (m0, m2, m0 + m3, m1 + m2)))


def __starting_point():
    main()


__starting_point()
