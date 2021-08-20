def main():
    n = int(input())
    (ww, hh) = ([0] * n, [0] * n)
    for i in range(n):
        (w, h) = map(int, input().split())
        (ww[i], hh[i]) = (w, h)
    hi = sorted(range(n), key=hh.__getitem__)
    width = sum(ww)
    height = hh[hi[-1]]
    for i in hi[:-1]:
        ww[i] = (width - ww[i]) * height
    i = hi[-1]
    ww[i] = (width - ww[i]) * hh[hi[-2]]
    print(' '.join(map(str, ww)))


def __starting_point():
    main()


__starting_point()
