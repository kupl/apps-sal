def main():
    (r1, c1, r2, c2) = list(map(int, input().split()))
    (_1, _2, _3) = (2, 2, 0)
    if r1 == r2 or c1 == c2:
        _1 = 1
    if (r1 + c1) % 2 != (r2 + c2) % 2:
        _2 = 0
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
        _2 = 1
    _3 = max(abs(r1 - r2), abs(c1 - c2))
    print(_1, _2, _3)


def __starting_point():
    main()


__starting_point()
