import sys
import math
import queue
import bisect
MOD = 10**9 + 7
sys.setrecursionlimit(1000000)

n = int(input())
a = list(map(int, input().split()))
s = 0
for ai in a:
    s += ai % 2
if s == 0 or s == n:
    print(*a)
else:
    print(*sorted(a))
