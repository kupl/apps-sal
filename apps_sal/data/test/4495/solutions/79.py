import math
import collections
from itertools import product


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


(a, b, x) = mi()
if a % x != 0:
    A = x * (a // x + 1)
else:
    A = a
B = b - b % x
print((B - A) // x + 1)
