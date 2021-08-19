def fallen_snow(a, b):
    return (b - a) * (b - a + 1) // 2 - b


def main():
    (a, b) = map(int, input().split())
    print(fallen_snow(a, b))


def __starting_point():
    main()


__starting_point()
