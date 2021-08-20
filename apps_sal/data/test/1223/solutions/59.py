def f_e():
    (n, *p) = list(map(int, open(0).read().split()))
    p = sorted([(v, i) for (i, v) in enumerate(p)])
    (*l,) = list(range(-1, n - 1))
    (*r,) = list(range(1, n + 1))
    a = 0
    for (v, i) in p:
        (l0, r0) = (l[i], r[i])
        l1 = l[l0] if l0 > -1 else l0
        r1 = r[r0] if r0 < n else r0
        a += ((l0 - l1) * (r0 - i) + (r1 - r0) * (i - l0)) * v
        if l0 > -1:
            r[l0] = r0
        if r0 < n:
            l[r0] = l0
    print(a)


def __starting_point():
    f_e()


__starting_point()
