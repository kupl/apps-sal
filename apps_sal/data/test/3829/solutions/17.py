def main():
    (m, n) = map(int, input().split())
    print(m - sum(((i / m) ** n for i in range(m))))


def __starting_point():
    main()


__starting_point()
