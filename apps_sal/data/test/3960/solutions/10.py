def main():
    input()
    aa = list(map(int, input().split()))
    (a, s) = (aa[0], 1)
    u = c = mi = ma = 0
    for b in aa:
        c += abs(a - b) * s
        a = b
        s *= -1
        if ma < c:
            ma = c
            u = ma - mi
        elif mi > c:
            mi = c
    (a, s) = (aa[0], -1)
    v = c = mi = ma = 0
    for b in aa:
        c += abs(a - b) * s
        a = b
        s *= -1
        if ma < c:
            ma = c
            v = ma - mi
        elif mi > c:
            mi = c
    print(max(u, v))


def __starting_point():
    main()


__starting_point()
