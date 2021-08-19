import math
import collections
from itertools import product


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


l = li()
l.sort()
print(l[0] * l[1] // 2)
