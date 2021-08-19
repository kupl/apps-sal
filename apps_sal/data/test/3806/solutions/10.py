def main():
    (n, a, b) = list(map(int, input().split()))
    (l, res) = ([], [])
    for _ in range(n):
        (u, v) = input().split()
        l.append((int(u) - a, int(v) - b))
    (x0, y0) = l[-1]
    for (x1, y1) in l:
        res.append(x1 * x1 + y1 * y1)
        (dx, dy) = (x1 - x0, y1 - y0)
        if (x0 * dx + y0 * dy) * (x1 * dx + y1 * dy) < 0:
            x0 = x0 * y1 - x1 * y0
            res.append(x0 * x0 / (dx * dx + dy * dy))
        (x0, y0) = (x1, y1)
    print((max(res) - min(res)) * 3.141592653589793)


def __starting_point():
    main()


__starting_point()
