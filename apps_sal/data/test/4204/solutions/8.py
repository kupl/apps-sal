from fractions import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import math
import sys
sys.setrecursionlimit(10000000)
mod = 998244353


def readInts():
    return list(map(int, input().split()))


def I():
    return int(input())


sys.setrecursionlimit(10000000)
mod = 10**9 + 7


def readInts():
    return list(map(int, input().split()))


def I():
    return int(input())


s = input()
k = I()
where = 0
while where < len(s):
    if s[where] == '1':
        where += 1
    else:
        break
print(('1' if k <= where else s[where]))
