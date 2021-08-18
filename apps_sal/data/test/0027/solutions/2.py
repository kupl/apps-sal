import getpass
import sys
import math
import random
import itertools
import bisect
import time

files = True
debug = False

if getpass.getuser() == 'frohenk' and files:
    debug = True
    sys.stdin = open("test.in")
elif files:
    pass


def lcm(a, b):
    return a * b // math.gcd(a, b)


def ria():
    return [int(i) for i in input().split()]


def range_sum(a, b):
    ass = (((b - a + 1) // 2) * (a + b))
    if (a - b) % 2 == 0:
        ass += (b - a + 2) // 2
    return ass


def comba(n, x):
    return (math.factorial(n) // math.factorial(n - x)) // math.factorial(x)


n = ria()[0]
suma = n
st = input()
mx = 0
for i in range(1, n + 1):
    if i + i <= n:
        if st[:i] == st[i:i + i]:
            mx = max(mx, len(st[:i]) - 1)
print(n - mx)
