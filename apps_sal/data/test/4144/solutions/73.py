def __starting_point():
    n = int(input())
    print((10 ** n - 2 * 9 ** n + 8 ** n) % (10 ** 9 + 7))


__starting_point()
