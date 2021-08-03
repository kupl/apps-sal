def main():
    v = int(input())
    l = list((w, 9 - d) for d, w in enumerate(map(int, input().split())))
    w, d0 = min(l)
    le = v // w
    if not le:
        print(-1)
        return
    res = [str(10 - d0)] * le
    v -= w * le
    base, start = w, 0
    l = sorted(((10 - d, w - base) for w, d in l if d < d0))
    while l:
        d, w = l.pop()
        delta = v // w
        res[start:start + delta] = [str(d)] * delta
        start += delta
        v -= w * delta
    print(''.join(res))


def __starting_point():
    main()


__starting_point()
