import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


A, B, C, D = map(int, input().split())
ans = 0

Ac = (A - 1) // C
Ad = (A - 1) // D
Acd = (A - 1) // lcm(C, D)
Bc = B // C
Bd = B // D
Bcd = B // lcm(C, D)

c = Bc - Ac
d = Bd - Ad
cd = Bcd - Acd

print(B - A + 1 - (c + d - cd))
