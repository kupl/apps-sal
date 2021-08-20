import getpass
import sys
import math
from decimal import Decimal
import decimal
files = True
debug = False
if getpass.getuser() == 'frohenk' and files:
    debug = True
    sys.stdin = open('test.in')
elif files:
    pass


def lcm(a, b):
    return a * b // math.gcd(a, b)


def ria():
    return [int(i) for i in input().split()]


def range_sum(a, b):
    ass = (b - a + 1) // 2 * (a + b)
    if (a - b) % 2 == 0:
        ass += (b - a + 2) // 2
    return ass


def comba(n, x):
    return math.factorial(n) // math.factorial(n - x) // math.factorial(x)


(h, m) = ria()
time = h * 60 + m
offerTime = max(20 * 60 - time, 0)
(h, d, c, n) = ria()
mini = math.ceil(h / n) * c
h += offerTime * d
mini = min(math.ceil(h / n) * c * 0.8, mini)
print(mini)
