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
mod = 10**9 + 7
INF = float('inf')
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


H, W, M = readInts()

dic1 = Counter()
dic2 = Counter()
s = set()
for i in range(M):
    h, w = [int(x) - 1 for x in input().split()]
    dic1[h] += 1
    dic2[w] += 1
    s.add((h, w))
ans = 0

for h, w in s:
    ans = max(ans, dic1[h] + dic2[w] - 1)

dic1 = dic1.most_common()
dic2 = dic2.most_common()
max1 = dic1[0][1]
max2 = dic2[0][1]

for k1, v1 in dic1:
    if v1 < max1:
        break
    for k2, v2 in dic2:
        if v2 < max2:
            break
        if (k1, k2) in s:
            continue
        ans = max(ans, v1 + v2)
        break
print(ans)
