from math import gcd


def lcm(a, b):
    return a // gcd(a, b) * b


def getExclude(x, c, d):
    return x - x // c - x // d + x // lcm(c, d)


(a, b, c, d) = (int(x) for x in input().split())
ans = getExclude(b, c, d) - getExclude(a - 1, c, d)
print(ans)
