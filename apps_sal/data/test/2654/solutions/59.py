# float型を許すな
# numpyはpythonで
from math import floor, ceil, pi, factorial
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, accumulate, groupby, product
from collections import defaultdict
from collections import Counter, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str, x))))


inf = 10**17
mod = 10**9 + 7

n = I()
lis1 = []
lis2 = []
for i in range(n):
    a, b = MI()
    lis1.append(a)
    lis2.append(b)
lis1.sort()
lis2.sort()
if n % 2 == 1:
    med1 = lis1[n // 2]
    med2 = lis2[n // 2]
    print(med2 - med1 + 1)
if n % 2 == 0:
    med1 = lis1[n // 2 - 1] + lis1[n // 2]
    med2 = lis2[n // 2 - 1] + lis2[n // 2]
    print(med2 - med1 + 1)
