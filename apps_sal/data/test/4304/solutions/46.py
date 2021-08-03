def main():
    a, b = list(map(int, input().split()))
    diff = b - a
    high_a = sum(list(range(1, diff)))
    print((high_a - a))


def __starting_point():
    main()


__starting_point()
