from fractions import gcd
from itertools import combinations, permutations, accumulate
from collections import deque, defaultdict, Counter
import decimal
import re
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7


def readInts():
    return list(map(int, input().split()))


def I():
    return int(input())


n = I()
A = readInts()
left = 0
right = sum(A)
MIN = float('inf')
for i in range(n - 1):
    left += A[i]
    right -= A[i]
    MIN = min(MIN, abs(left - right))
print(MIN)
