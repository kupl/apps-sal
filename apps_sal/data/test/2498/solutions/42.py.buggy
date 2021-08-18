from math import gcd
from functools import reduce

n, m = map(int, input().split())
a = list(map(int, input().split()))


def lcm(a, b):
    return a * b // gcd(a, b)


a = [i // 2 for i in a]

l = reduce(lcm, a)

if any((l // i) % 2 == 0 for i in a):
    print(0)
    return

print(-(-(m // l) // 2))
