import math
a, b, c, d = map(int, input().split())

# 2数を受け取って最小公倍数を返す関数


def lcm(a, b):
    y = a * b / math.gcd(a, b)
    return int(y)


x = (b - a) + 1

# cの倍数の数
cc = (b // c) - ((a - 1) // c)

# dの倍数の数
dd = (b // d) - ((a - 1) // d)

# cとdの倍数の数
cd = lcm(c, d)
cd = (b // cd) - ((a - 1) // (cd))

# cとdの和集合
wa = (cc - cd) + dd

print(x - wa)
