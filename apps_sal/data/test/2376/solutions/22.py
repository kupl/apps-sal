# coding: utf-8
# hello worldと表示する
# float型を許すな
# numpyはpythonで
from math import floor, ceil, pi, factorial, sqrt
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
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print(('\n'.join(x)))
def printni(x): print(('\n'.join(list(map(str, x)))))


inf = 10**17
mod = 10**9 + 7

n, w = MI()
lis = [LI() for i in range(n)]
u = lis[0][0]
vals = [[] for i in range(4)]
for i in range(n):
    if lis[i][0] == u:
        vals[0].append(lis[i][1])
    elif lis[i][0] == u + 1:
        vals[1].append(lis[i][1])
    elif lis[i][0] == u + 2:
        vals[2].append(lis[i][1])
    else:
        vals[3].append(lis[i][1])
# print(vals)
for i in range(4):
    vals[i].sort(reverse=True)
    vals[i] = list(accumulate(vals[i]))
    vals[i] = [0] + vals[i]
mx = 0
# print(vals)
for i in range(len(vals[0])):
    for j in range(len(vals[1])):
        for k in range(len(vals[2])):
            for l in range(len(vals[3])):
                if u * i + (u + 1) * j + (u + 2) * k + (u + 3) * l > w:
                    continue
                V = vals[0][i] + vals[1][j] + vals[2][k] + vals[3][l]
                if V > mx:
                    mx = V
print(mx)
