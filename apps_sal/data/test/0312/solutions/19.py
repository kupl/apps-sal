def main():
    (n, m) = [int(t) for t in input().split()]
    if n == 1:
        print(1)
    elif m <= n / 2.0:
        print(m + 1)
    else:
        print(m - 1)


def __starting_point():
    main()


__starting_point()
