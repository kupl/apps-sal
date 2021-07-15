from functools import reduce
from math import gcd

def lcm(n, c, d):
    g = gcd(c, d)
    l = c // g * d
    return n - (n // c) - (n // d) + n //l

a, b, c, d = map(int, input().split())
print(lcm(b, c, d) - lcm(a-1, c, d))
