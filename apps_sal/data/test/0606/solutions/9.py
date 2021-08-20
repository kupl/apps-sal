eps = 1e-14
(R, x1, y1, x2, y2) = map(int, input().split())
rst = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** (1 / 2)
if rst > R:
    print(x1, y1, R - eps)
else:
    of = rst
    r = (R + of) / 2
    dx = x1 - x2
    dy = y1 - y2
    if of != 0:
        dx1 = (1 / 2 + R / (2 * of)) * dx
        dy1 = (1 / 2 + R / (2 * of)) * dy
    else:
        dx1 = R / 2
        dy1 = 0
    x = x2 + dx1
    y = y2 + dy1
    print(x, y, r - eps)
