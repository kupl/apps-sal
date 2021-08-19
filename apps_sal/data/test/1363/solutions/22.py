def C(n, k):
    if n < k:
        return 0
    if k == 1:
        return n
    elif k == 2:
        return n * (n - 1) // 2
    elif k == 3:
        return n * (n - 1) * (n - 2) // 6


def main():
    (g, d, f) = [int(_) for _ in input().split()]
    gs = [int(_) for _ in input().split()]
    ds = [int(_) for _ in input().split()]
    fs = [int(_) for _ in input().split()]
    ans = 0
    gs.sort()
    ds.sort()
    fs.sort()
    (gmin, dmin, fmin) = (0, 0, 0)
    (gmax, dmax, fmax) = (0, 0, 0)
    while g - gmin >= 1 and d - dmin >= 2 and (f - fmin >= 3):
        term = 1
        mn = min(gs[gmin], ds[dmin], fs[fmin])
        while gmax < g and gs[gmax] <= mn * 2:
            gmax += 1
        gn = gmax - gmin
        if mn == gs[gmin]:
            term *= 1
            gmin += 1
        else:
            term *= C(gn, 1)
        while dmax < d and ds[dmax] <= mn * 2:
            dmax += 1
        dn = dmax - dmin
        if mn == ds[dmin]:
            term *= C(dn - 1, 1)
            dmin += 1
        else:
            term *= C(dn, 2)
        while fmax < f and fs[fmax] <= mn * 2:
            fmax += 1
        fn = fmax - fmin
        if mn == fs[fmin]:
            term *= C(fn - 1, 2)
            fmin += 1
        else:
            term *= C(fn, 3)
        ans += term
    print(ans)


def print_test():
    from random import randint
    (g, d, f) = (200, 400, 600)
    print(g, d, f)
    for _ in range(g):
        print(randint(1, 100000), end=' ')
    print()
    for _ in range(d):
        print(randint(1, 100000), end=' ')
    print()
    for _ in range(f):
        print(randint(1, 100000), end=' ')
    print()


def __starting_point():
    main()


__starting_point()
