(m, b) = list(map(int, input().split()))


def f(n):
    return n * (n + 1) // 2


def g(y):
    x = m * (b - y)
    return f(x) * (y + 1) + f(y) * (x + 1)


print(max((g(y) for y in range(b + 1))))
