def main():
    a, b, n = map(int, input().split())
    x = min(b - 1, n)
    floor1 = int(a * x / b)
    floor2 = int(x / b)
    print(floor1 - floor2)


def __starting_point():
    main()


__starting_point()
