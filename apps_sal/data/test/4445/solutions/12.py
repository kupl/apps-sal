from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import *
from itertools import *
import functools
import sys
import math
import random
MAX = sys.maxsize
MAXN = 10 ** 5 + 10
MOD = 10 ** 9 + 7


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)


def numIN(x=' '):
    return map(int, sys.stdin.readline().strip().split(x))


def charIN():
    return sys.stdin.readline().strip().split()


def dis(x, y):
    a = y[0] - x[0]
    b = x[1] - y[1]
    return (a * a + b * b) ** 0.5


n = int(input())
l = list(numIN())
e = []
o = []
for i in l:
    if i % 2:
        o.append(i)
    else:
        e.append(i)
if len(e) == len(o):
    print(0)
else:
    e.sort(reverse=True)
    o.sort(reverse=True)
    mn = min(len(e), len(o))
    x = e[mn:]
    y = o[mn:]
    if x:
        print(sum(x) - x[0])
    else:
        print(sum(y) - y[0])
