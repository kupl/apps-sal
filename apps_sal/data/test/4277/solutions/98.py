def main():
    (n, a, b) = list(map(int, input().split()))
    print(min(n * a, b))
    pass


def __starting_point():
    main()


__starting_point()
