import sys
import heapq as hq
import itertools
import math
import collections
ma = lambda: map(int, input().split())
lma = lambda: list(map(int, input().split()))
tma = lambda: tuple(map(int, input().split()))
ni = lambda: int(input())
yn = lambda fl: print("Yes") if fl else print("No")
n, T = ma()
ans = 10**15
for i in range(n):
    c, t = ma()
    if t <= T:
        ans = min(ans, c)
if ans == 10**15:
    print("TLE")
else: print(ans)
