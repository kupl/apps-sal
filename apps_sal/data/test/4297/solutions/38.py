import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


n = int(input())
print(lcm(2, n))
