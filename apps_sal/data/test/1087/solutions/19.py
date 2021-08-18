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

n, k = MI()
lis = LI()
u = max(max(lis), k)
memo = 0
for i in range(45):
    x = (u >> i) % 2
    if x == 1:
        memo = i
memo += 1
table = [0 for i in range(memo)]
for i in range(n):
    for j in range(memo):
        x = (lis[i] >> j) % 2
        if x == 1:
            table[j] += 1
table2 = [[0, 0] for i in range(memo)]
for i in range(memo):
    table2[i][0] = abs(n - 2 * table[i]) * 2**i
    table2[i][1] = i + 1
    if n - 2 * table[i] < 0:
        table2[i][1] *= (-1)
table2.sort(reverse=True)
maxx = 0
ans_table = [0 for i in range(memo)]
for i in range(memo):
    if table2[i][1] > 0:
        maxx += 2**(table2[i][1] - 1)
        if maxx <= k:
            ans_table[table2[i][1] - 1] = 1
        else:
            ans_table[table2[i][1] - 1] = 0
            maxx -= 2**(table2[i][1] - 1)
    else:
        ans_table[abs(table2[i][1]) - 1] = 0
ans = 0
for i in range(memo):
    if ans_table[i] == 1:
        ans += (2**i) * (n - table[i])
    else:
        ans += (2**i) * table[i]
print(ans)
