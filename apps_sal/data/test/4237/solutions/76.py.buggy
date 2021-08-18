import math
a, b, c, d = list(map(int, input().split()))


def calc(x):
    nonlocal c, d
    l = c // math.gcd(c, d) * d
    return x - x // c - x // d + x // l


print((calc(b) - calc(a - 1)))
