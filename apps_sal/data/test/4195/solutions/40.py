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


def rf():
    return list(map(float, sys.stdin.readline().split()))


def rl():
    return list(map(int, sys.stdin.readline().split()))


inf = float('inf')
mod = 10 ** 9 + 7
(d, n) = rm()
if n != 100:
    print((n - (n - 1) // 99) * 100 ** d)
else:
    print(101 * 100 ** d)
