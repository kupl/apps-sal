def __starting_point():
    n = int(input())
    if n == 0:
        print(1)
    else:
        print(1 + 3 * n * (n + 1))


__starting_point()
