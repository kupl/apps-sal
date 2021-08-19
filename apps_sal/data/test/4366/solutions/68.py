def main():
    (a, b) = map(int, input().split())
    if a + b < 24:
        print(a + b)
    else:
        print(a + b - 24)


def __starting_point():
    main()


__starting_point()
