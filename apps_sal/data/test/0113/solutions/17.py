import math


def ria():
    return [int(i) for i in input().split()]


n, k = ria()

g = math.gcd(n, 10**k)
print(n * (10**k) // g)
