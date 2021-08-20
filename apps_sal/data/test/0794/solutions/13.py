import sys
import math
import queue
import bisect
MOD = 10 ** 9 + 7
sys.setrecursionlimit(1000000)
n = int(input())
a = list(map(int, input().split()))
a.sort()
if sum(a[:n]) == sum(a[n:]):
    print(-1)
else:
    print(*a)
