def abc063_d():
    (n, a, b) = map(int, input().split())
    H = [int(input()) for _ in range(n)]
    (lower, upper) = (0, 10 ** 16)
    d = a - b
    while upper - lower > 1:
        x = (upper + lower) // 2
        v = 0
        for hi in H:
            v += (max(0, hi - x * b) + d - 1) // d
        if v <= x:
            upper = x
        else:
            lower = x
    print(upper)


def __starting_point():
    abc063_d()


__starting_point()
