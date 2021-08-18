def __starting_point():
    a, b, x = list(map(int, input().split()))
    c = b // x - a // x
    if a % x == 0:
        c = c + 1
    print(c)


__starting_point()
