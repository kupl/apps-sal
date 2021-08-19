import math
import sys
from bisect import bisect_right, bisect_left, insort_right
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import accumulate, permutations, combinations
from sys import stdout


def R():
    return map(int, input().split())


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
cst = [math.inf] * n + [0]
for i in range(n):
    cst[i] = min(cst[i - 1] + 20, cst[bisect_left(arr, arr[i] - 89) - 1] + 50, cst[bisect_left(arr, arr[i] - 1439) - 1] + 120)
for i in range(n):
    print(cst[i] - cst[i - 1])
