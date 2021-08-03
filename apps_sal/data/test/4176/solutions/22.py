import math


def L():
    return list(map(int, input().split()))


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


[a, b] = L()

print(lcm(a, b))
