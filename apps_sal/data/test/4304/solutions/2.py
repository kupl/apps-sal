def main():
    (a, b) = list(map(int, input().split()))
    print(sum(list(range(1, b - a))) - a)


def __starting_point():
    main()


__starting_point()
