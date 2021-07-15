#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print(('\n'.join(x)))
def printni(x): print(('\n'.join(list(map(str,x)))))
inf = 10**17
mod = 10**9 + 7
s=SI()
n=len(s)
for i in range(n-1):
    if s[i]==s[i+1]:
        print((i+1,i+2))
        return
for i in range(n-2):
    if s[i]==s[i+2]:
        print((i+1,i+3))
        return
print((-1,-1))

