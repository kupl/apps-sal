def main():
    n = min(list(map(int, input().split())))
    print(n + 1)
    for (x, y) in zip(list(range(n + 1)), list(range(n, -1, -1))):
        print(x, y)


def __starting_point():
    main()


__starting_point()
