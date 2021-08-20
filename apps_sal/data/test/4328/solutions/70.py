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


(a, b) = readInts()
print(a + b if b % a == 0 else b - a)
