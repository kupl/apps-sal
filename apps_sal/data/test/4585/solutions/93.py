from fractions import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import sys
sys.setrecursionlimit(10000000)
mod = 998244353


def readInts():
    return list(map(int, input().split()))


def I():
    return int(input())


x = I()
t = 0
while (t * (t + 1)) / 2 < x:
    t += 1
print(t)
