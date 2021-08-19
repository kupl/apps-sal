import math
(a, b, c, d) = map(int, input().split())
n = b - a + 1


def lcm(x, y):
    return x * y // math.gcd(x, y)


x = lcm(c, d)
cc = b // c - (a - 1) // c
dc = b // d - (a - 1) // d
xc = b // x - (a - 1) // x
print(n - cc - dc + xc)
