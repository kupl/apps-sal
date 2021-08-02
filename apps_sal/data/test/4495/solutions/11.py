def main():
    a, b, x = list(map(int, input().split()))
    print((b // x - (a - 1) // x))


def __starting_point():
    main()


__starting_point()
