import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def div2_n(x):
    n = 0
    while x % 2 == 0:
        if x % 2 == 0:
            n += 1
            x >>= 1
    return n


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

a2 = [i // 2 for i in a]
n0 = div2_n(a2[0])
for i in range(1, n):
    if div2_n(a2[i]) != n0:
        print((0))
        return

a2_l = lcm(*a2)
print((m // a2_l - m // (a2_l * 2)))
