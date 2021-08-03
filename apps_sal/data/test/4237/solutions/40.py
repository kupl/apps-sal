import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


a, b, c, d = map(int, input().split())

l = lcm(c, d)
ans = (b - a + 1) - ((b // c + b // d - b // l) - ((a - 1) // c + (a - 1) // d - (a - 1) // l))
print(ans)
