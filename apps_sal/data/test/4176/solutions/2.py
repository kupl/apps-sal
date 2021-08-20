from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


(a, b) = list(map(int, input().split()))
print(lcm(a, b))
