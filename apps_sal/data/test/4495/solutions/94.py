a, b, x = list(map(int, input().split()))


def f(n, d):
    if n == -1:
        return 0
    return n // d + 1


print((f(b, x) - f(a - 1, x)))
