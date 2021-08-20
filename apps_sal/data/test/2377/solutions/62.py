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


(n, h) = readInts()
A = [0] * n
B = [0] * n
for i in range(n):
    (a, b) = readInts()
    A[i] = a
    B[i] = b
A = sorted(A, reverse=True)
B = sorted(B, reverse=True)
MAX = A[0]
ans = 0
for v in B:
    if h <= 0:
        break
    if v > MAX:
        ans += 1
        h -= v
    else:
        break
if h > 0:
    ans += (h + MAX - 1) // MAX
print(ans)
