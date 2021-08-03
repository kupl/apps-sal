import math
import functools


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


n = int(input())
t = [int(input()) for i in range(n)]
a = functools.reduce(math.gcd, t)
print(functools.reduce(lcm, t))
