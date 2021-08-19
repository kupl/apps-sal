from fractions import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import sys
sys.setrecursionlimit(10000000)
mod = 10 ** 9 + 7


def readInts():
    return list(map(int, input().split()))


def I():
    return int(input())


n = I()
A = readInts()
four = 0
two = 0
for i in range(n):
    if A[i] % 4 == 0:
        four += 1
    elif A[i] % 2 == 0:
        two += 1
print('Yes' if four + two // 2 >= n // 2 else 'No')
