def __starting_point():
    (a, b, c, d) = [int(x) for x in input().split()]
    (a, b, c) = sorted([a, b, c])
    print(max(a - (b - d), 0) + max(0, b + d - c))


__starting_point()
