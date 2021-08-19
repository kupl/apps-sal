def main():
    (R, x1, y1, x2, y2) = list(map(int, input().split()))
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 >= R ** 2:
        return (x1, y1, R)
    if x1 == x2 and y1 == y2:
        return (x1 + 0.5 * R, y1, 0.5 * R)
    vx = x1 - x2
    vy = y1 - y2
    vnorm = (vx ** 2 + vy ** 2) ** 0.5
    r = R / vnorm
    return (0.5 * (x1 + x2 + vx * r), 0.5 * (y1 + y2 + vy * r), 0.5 * (R + vnorm))


def __starting_point():
    (x, y, R) = main()
    print(x, y, R)


__starting_point()
