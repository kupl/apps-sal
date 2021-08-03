import sys
import heapq as hq
import itertools
import math
import collections
def ma(): return map(int, input().split())
def lma(): return list(map(int, input().split()))
def tma(): return tuple(map(int, input().split()))
def ni(): return int(input())
def yn(fl): return print("Yes") if fl else print("No")


n, T = ma()
ans = 10**15
for i in range(n):
    c, t = ma()
    if t <= T:
        ans = min(ans, c)
if ans == 10**15:
    print("TLE")
else:
    print(ans)
