from math import sqrt


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2) + 10**(-7)


def max_dist(p, x, y):
    res = 0
    for i in range(len(p)):
        dis = dist(p[i][0], p[i][1], x, y)
        if res < dis:
            res = dis
    return res


def calc(p, x):
    yL, yR = 0, 1000
    while yL + 10**-7 < yR:
        yl, yr = (2 * yL + yR) / 3, (yL + 2 * yR) / 3
        ql, qr = max_dist(p, x, yl), max_dist(p, x, yr)
        if ql < qr:
            yR = yr
        else:
            yL = yl
    return qr, yR


def main():
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    xL, xR = 0, 1000
    while xL + 10**-7 < xR:
        xl, xr = (2 * xL + xR) / 3, (xL + 2 * xR) / 3
        ql, yl = calc(p, xl)
        qr, yr = calc(p, xr)
        if ql < qr:
            xR = xr
        else:
            xL = xl
    print(max_dist(p, xR, yr))


def __starting_point():
    main()


__starting_point()
