from sys import stdin
from math import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import math
import bisect
import heapq
import sys
sys.setrecursionlimit(10000000)
mod = 10 ** 9 + 7
INF = float('inf')
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


n = I()
dic = defaultdict(int)
for i in range(n):
    a = I()
    dic[a] += 1
ans = 0
for (k, v) in list(dic.items()):
    ans += v % 2
print(ans)
