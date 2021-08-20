import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
from functools import reduce


def rr():
    return sys.stdin.readline().rstrip()


def rs():
    return sys.stdin.readline().split()


def ri():
    return int(sys.stdin.readline())


def rm():
    return list(map(int, sys.stdin.readline().split()))


def rl():
    return list(map(int, sys.stdin.readline().split()))


inf = float('inf')
mod = 10 ** 9 + 7
x = ri()
max_ = 0
for i in range(int(x ** 0.5), 0, -1):
    for j in range(1, 10):
        if i ** j <= x:
            max_ = max(i ** j, max_)
        else:
            break
print(max_)
