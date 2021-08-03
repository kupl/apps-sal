def main():
    n, m = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    res = max(aa) - min(aa)
    ll, rr = [n + 1], [n + 1]
    segments = res_segments = [False] * (m + 1)
    bounds = {0, n, n + 1}
    for _ in range(m):
        l, r = list(map(int, input().split()))
        l -= 1
        ll.append(l)
        rr.append(r)
        bounds.add(l)
        bounds.add(r)
    xlat = sorted(bounds)
    mi, ma = [], []
    for l, r in zip(xlat, xlat[1:-1]):
        t = aa[l:r]
        mi.append(min(t))
        ma.append(max(t))
    bounds = {x: i for i, x in enumerate(xlat)}
    for xx in (ll, rr):
        for i, x in enumerate(xx):
            xx[i] = bounds[x]
    il, ir = (sorted(list(range(m + 1)), key=xx.__getitem__, reverse=True) for xx in (ll, rr))
    for i in range(len(xlat) - 1):
        while True:
            k = il[-1]
            lo = ll[k]
            if lo > i:
                break
            segments[k] = True
            for j in range(lo, rr[k]):
                mi[j] -= 1
                ma[j] -= 1
            del il[-1]

        x = max(ma) - min(mi)
        if res < x:
            res = x
            res_segments = segments[:]
        while True:
            k = ir[-1]
            hi = rr[k]
            if hi > i:
                break
            segments[k] = False
            for j in range(ll[k], hi):
                mi[j] += 1
                ma[j] += 1
            del ir[-1]

    print(res)
    segments = [i for i, f in enumerate(res_segments) if f]
    print(len(segments))
    print(*segments)


def __starting_point():
    main()


__starting_point()
