from sys import stdin
from fractions import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import math
import sys
sys.setrecursionlimit(10000000)
mod = 10 ** 9 + 7
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


(a, b, n) = readInts()
th = b - 1
if n >= th:
    print(int(math.floor(a * th / b) - a * math.floor(th / b)))
else:
    print(int(math.floor(a * n / b) - a * math.floor(n / b)))
