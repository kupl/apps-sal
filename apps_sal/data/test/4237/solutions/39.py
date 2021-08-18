from math import gcd


def count(x, c, d):
    lcm = c // gcd(c, d) * d
    return x - x // c - x // d + x // lcm


a, b, c, d = list(map(int, input().split()))
print((count(b, c, d) - count(a - 1, c, d)))
