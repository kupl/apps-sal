def C(n, m):
    a = 1
    b = 1
    for i in range(1, m + 1):
        a *= n + 1 - i
        b *= i
    return a // b


def __starting_point():
    n = int(input())
    print(C(n, 5) * n * (n - 1) * (n - 2) * (n - 3) * (n - 4))


__starting_point()
