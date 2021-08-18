from functools import reduce
import math
n = int(input())


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(numbers):
    return reduce(lcm_base, numbers, 1)


t = []
for i in range(n):
    t.append(int(input()))

print(lcm(t))
