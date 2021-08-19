import math
(a, b, c, d) = map(int, input().split())


def lcm(a, b):
    y = a * b / math.gcd(a, b)
    return int(y)


x = b - a + 1
cc = b // c - (a - 1) // c
dd = b // d - (a - 1) // d
cd = lcm(c, d)
cd = b // cd - (a - 1) // cd
wa = cc - cd + dd
print(x - wa)
