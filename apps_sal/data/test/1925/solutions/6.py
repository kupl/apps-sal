import math
(a, b, n) = map(int, input().split())


def f(x, a, b):
    return math.floor(a * x / b) - a * math.floor(x / b)


x = min(n, b - 1)
print(f(x, a, b))
