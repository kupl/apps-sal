from math import floor


def f(x):
    return floor(a * x / b) - a * floor(x / b)


a, b, n = map(int, input().split())
print(f(min(b - 1, n)))
