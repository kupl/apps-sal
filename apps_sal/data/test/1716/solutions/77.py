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

n, m, que = MI()
lis = [[0] * n for i in range(n)]
for i in range(m):
    l, r = MI()
    lis[l - 1][r - 1] += 1
for i in range(n):
    lis[i] = list(accumulate(lis[i]))
for i in range(n):
    for j in range(n - 1):
        lis[j + 1][i] += lis[j][i]
for i in range(que):
    p, q = MI()
    if p == 1:
        ans = lis[q - 1][q - 1]
    else:
        ans = lis[q - 1][q - 1] - lis[p - 2][q - 1]
    print(ans)
