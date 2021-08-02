from math import ceil, floor


def main():
    h, w = list(map(int, input().split()))
    d = h * w
    d = min((ceil(h / 3) - floor(h / 3)) * w, d)
    d = min((ceil(w / 3) - floor(w / 3)) * h, d)
    dd = h * w
    for i in range(h):
        u = i * w
        d1 = (h - i) * ceil(w / 2)
        d2 = (h - i) * floor(w / 2)
        di = max(abs(u - d1), abs(u - d2))
        if di > dd:
            break
        dd = di
    d = min(dd, d)
    dd = h * w
    for i in range(w):
        u = i * h
        d1 = (w - i) * ceil(h / 2)
        d2 = (w - i) * floor(h / 2)
        di = max(abs(u - d1), abs(u - d2))
        if di > dd:
            break
        dd = di
    d = min(dd, d)
    print(d)


def __starting_point():
    main()


__starting_point()
