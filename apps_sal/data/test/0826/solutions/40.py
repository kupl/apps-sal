n = int(input())


def sqrt(n):
    if n == 0:
        return 0
    x = 1 << (n.bit_length() + 1) // 2
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def f(n):
    return


print(n + 1 - (-1 + sqrt(1 + 8 * (n + 1))) // 2)
