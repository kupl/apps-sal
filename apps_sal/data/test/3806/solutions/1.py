from math import hypot, pi, copysign


def main():
    n, a, b = list(map(int, input().split()))
    l, res = [], []
    for _ in range(n):
        x0, y0 = list(map(int, input().split()))
        l.append((x0 - a, y0 - b))
    x0, y0 = l[-1]
    for x1, y1 in l:
        res.append(hypot(x1, y1))
        dx, dy = x1 - x0, y1 - y0
        if copysign(1., x0 * dx + y0 * dy) != copysign(1., x1 * dx + y1 * dy):
            res.append(abs(x0 * y1 - x1 * y0) / hypot(dx, dy))
        x0, y0 = x1, y1
    print((max(res) ** 2 - min(res) ** 2) * pi)


def __starting_point():
    main()


__starting_point()
