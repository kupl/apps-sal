def main():
    n, m = map(int, input().split())

    time = 1900 * m + 100 * (n - m)
    power = 2 ** m
    print(time * power)


def __starting_point():
    main()


__starting_point()
