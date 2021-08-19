def main():
    (n, m, k) = map(int, input().split())
    l = list((tuple(map(int, input().split())) for _ in range(k)))
    m += 1
    n += 1
    field = [False] * (m * n)
    patterns = ((1, m, m + 1), (-m, -m + 1, 1), (-1, -m - 1, -m), (-1, m - 1, m))
    for (i, (y, x)) in enumerate(l):
        yx = y * m + x - m - 1
        field[yx] = True
        if any((all((field[yx + _] for _ in pattern)) for pattern in patterns)):
            print(i + 1)
            return
    print(0)


def __starting_point():
    main()


__starting_point()
