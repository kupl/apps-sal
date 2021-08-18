def __starting_point():
    n = int(input())
    m = int(n / 2 + 1)
    print(m)
    for i in range(1, n + 1):
        if i <= m:
            print(1, i)
        else:
            print(i - m + 1, m)


__starting_point()
