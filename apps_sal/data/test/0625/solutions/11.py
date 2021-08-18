import sys


def x(y):
    return ((2 + y) * (y // 2) // 2)


def a(y):
    return (1 + y) * ((y + 1) // 2) // 2


n = int(input())
if n % 2 == 0:
    print(x(n) - a(n - 1))
else:
    print(-a(n) + x(n - 1))
