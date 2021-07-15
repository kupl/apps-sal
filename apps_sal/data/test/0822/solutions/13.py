import math


def ria():
    return [int(i) for i in input().split()]


n, m, z = ria()

print(z//(n*m//math.gcd(n,m)))
