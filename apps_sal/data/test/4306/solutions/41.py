def main():
    (a, b, c, d) = list(map(int, input().split()))
    print(max(0, min(b, d) - max(a, c)))


def __starting_point():
    main()


__starting_point()
