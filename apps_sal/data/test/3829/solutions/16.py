def main():
    m, n = map(int, input().split())
    print(sum((i + 1) * (((i + 1) / m) ** n - (i / m) ** n) for i in range(m)))


def __starting_point():
    main()
__starting_point()
