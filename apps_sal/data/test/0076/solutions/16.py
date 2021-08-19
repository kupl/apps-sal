import collections
from functools import cmp_to_key
import sys


def getIntList():
    return list(map(int, input().split()))


(n, m, a, b) = getIntList()
z = n % m
r = min((m - z) * a, z * b)
print(r)
