def a176(n, x, t):

    return int(-(-n // x) * t)


def main():
    n, x, t = map(int, input().split())
    print(a176(n, x, t))


def __starting_point():
    main()


__starting_point()
