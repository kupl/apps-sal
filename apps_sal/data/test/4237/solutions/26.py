from math import gcd


def f(x, c, d):
    res = x
    res -= x // c
    res -= x // d
    res += x // (c // gcd(c, d) * d)
    return res


(a, b, c, d) = map(int, input().split())
ans = f(b, c, d) - f(a - 1, c, d)
print(ans)
