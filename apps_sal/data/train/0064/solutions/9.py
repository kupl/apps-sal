def y():
    return [*map(int, input().split())]


for _ in range(int(input())):
    (n, t) = map(int, input().split())
    a = [0] + y() + [t]
    (l, h) = (0, n + 1)
    tl = th = 0
    while h - l > 1:
        dl = (a[l + 1] - a[l]) / (l + 1)
        dh = (a[h] - a[h - 1]) / (n + 2 - h)
        if tl + dl > th + dh:
            th += dh
            h -= 1
        else:
            tl += dl
            l += 1
    (sh, sl) = (n + 2 - h, l + 1)
    if tl > th:
        (tl, th) = (th, tl)
        (sh, sl) = (sl, sh)
    print(th + (a[h] - a[l] - (th - tl) * sl) / (sh + sl))
