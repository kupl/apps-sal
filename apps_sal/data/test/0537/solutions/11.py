def __starting_point():
    n, k = list(map(int, input().split()))
    c = n // ((k + 1) * 2)
    if c == 0:
        print(0, 0, n)
    else:
        print(c, k * c, n - (k + 1) * c)


__starting_point()
