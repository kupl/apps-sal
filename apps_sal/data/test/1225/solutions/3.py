import collections
import math
import sys


def N():
    return int(input())


def L():
    return list(map(int, input().split()))


def NL(n):
    return [list(map(int, input().split())) for i in range(n)]


mod = pow(10, 9) + 7
n = N()
l = int(math.log2(n))
su = 0
z = 1
for i in range(l + 1):
    su += z
    z *= 2
print(su)
