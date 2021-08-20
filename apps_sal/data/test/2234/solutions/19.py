import random


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b / gcd(a, b)


for _ in range(int(input())):
    (n, k) = map(int, input().split())
    if n >= k:
        print((n + k) % 2)
    else:
        print(k - n)
