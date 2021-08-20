def main():
    n = int(input())
    (ww, hh) = ([0] * n, [0] * n)
    for i in range(n):
        (w, h) = map(int, input().split())
        (ww[i], hh[i]) = (w, h)
    idx = max(range(n), key=hh.__getitem__)
    mx0 = hh[idx]
    hh[idx] = 1
    mx1 = max(hh)
    width = sum(ww)
    for (i, w) in enumerate(ww):
        if i == idx:
            ww[i] = (width - ww[i]) * mx1
        else:
            ww[i] = (width - ww[i]) * mx0
    print(' '.join(map(str, ww)))


def __starting_point():
    main()


__starting_point()
