n = int(input())


def cross_plots(x1, x2, y1, y2, r):
    dx, dy = x2 - x1, y2 - y1
    d = dx ** 2 + dy ** 2
    t = ((4 * (r ** 2) - d) / (4 * d)) ** 0.5
    nx, ny = -t * dy, t * dx

    return ((x1 + x2) / 2 + nx, (y1 + y2) / 2 + ny),\
           ((x1 + x2) / 2 - nx, (y1 + y2) / 2 - ny)


plots = [tuple(map(int, input().split())) for _ in range(n)]
l, r = 0, 2000
while r - l > 10 ** -7:
    R = (r + l) / 2
    cross = []
    flg = False
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = plots[i]
            x2, y2 = plots[j]
            dx, dy = x2 - x1, y2 - y1
            if dx ** 2 + dy ** 2 > 4 * (R ** 2):
                flg = True
                break

            p1, p2 = cross_plots(x1, x2, y1, y2, R)
            cross.append(p1)
            cross.append(p2)

    if flg:
        l = R
        continue

    for xc, yc in cross:
        if all((xc - x) ** 2 + (yc - y) ** 2 < R ** 2 + 10e-9 for x, y in plots):
            flg = True
            break

    if flg:
        r = R
    else:
        l = R


print(r)
