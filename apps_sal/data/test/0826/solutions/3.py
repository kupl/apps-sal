def resolve():
    n = int(input())
    l = 0
    r = 10 ** 18
    m = 0
    while l + 1 < r:
        m = (l + r) // 2
        if m * (m + 1) // 2 <= n + 1:
            l = m
        else:
            r = m
    print(n - l + 1)


def __starting_point():
    resolve()


__starting_point()
