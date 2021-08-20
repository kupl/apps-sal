import math
from functools import reduce
n = int(input())
a = list(map(int, input().split()))


def lcm(x, y):
    return x * y // math.gcd(x, y)


l = reduce(lcm, a)
b = list(map(lambda x: l // x, a))
m = 10 ** 9 + 7
print(sum(b) % m)
