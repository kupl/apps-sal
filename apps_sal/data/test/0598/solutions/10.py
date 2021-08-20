def main():
    (n, x) = list(map(int, input().split()))
    vouchers = [False] * x
    for _ in range(n):
        (lo, hi, cost) = list(map(int, input().split()))
        w = hi - lo
        if w < x:
            l = vouchers[w]
            if l:
                l.append((lo, cost))
            else:
                vouchers[w] = [(lo, cost)]
    best = inf = 1 << 31
    x -= 2
    if not x & 1 and vouchers[x // 2]:
        (lh, h) = (vouchers[x // 2], None)
        for f in (lh.sort, lh.reverse):
            l = h
            f()
            (h, b) = ([], inf)
            for (lo, cost) in lh:
                if b > cost:
                    b = cost
                    h.append((lo, b))
        (b, v) = h.pop()
        for (a, u) in l:
            a += w
            while a >= b and h:
                (b, v) = h.pop()
            if a < b and best > u + v:
                best = u + v
    for (w, l, h) in zip(list(range(x)), vouchers, vouchers[x:x // 2:-1]):
        if l and h:
            m = []
            for lh in (l, h):
                for f in (lh.sort, lh.reverse):
                    f()
                    (t, b) = ([], inf)
                    for (lo, cost) in lh:
                        if b > cost:
                            b = cost
                            t.append((lo, b))
                    m.append(t)
            for (l, h) in ((m[0], m[3]), (m[2], m[1])):
                (b, v) = h.pop()
                for (a, u) in l:
                    a += w
                    while a >= b and h:
                        (b, v) = h.pop()
                    if a < b and best > u + v:
                        best = u + v
                w = x - w
    print(best if best < inf else -1)


def __starting_point():
    main()


__starting_point()
