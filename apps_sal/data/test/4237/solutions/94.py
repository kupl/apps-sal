import math


def lcm(x, y):
    return x * y // math.gcd(x, y)


def f(x, c, d):
    res = x
    res -= x // c
    res -= x // d
    res += x // lcm(c, d)
    return res


(a, b, c, d) = map(int, input().split())
ans = f(b, d, c) - f(a - 1, c, d)
print(ans)
