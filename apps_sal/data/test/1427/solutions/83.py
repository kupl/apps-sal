from functools import reduce
from math import gcd

MOD = 10 ** 9 + 7

_ = int(input())
la = list(map(int, input().split()))


def inv(a):
    return pow(a, MOD - 2, MOD)


def lcm(a, b):
    return a * b // gcd(a, b)


def addmod(a, b):
    return (a + b) % MOD


l = reduce(lcm, la) % MOD
answer = reduce(addmod, (l * inv(a) for a in la), 0)
print(answer)
