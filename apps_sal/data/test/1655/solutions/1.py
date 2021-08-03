import math
import functools as ft
import itertools as it

n = int(input())
a = list(map(int, input().split()))
cur = a[-1]
res = 0
for i in range(len(a) - 2, -1, -1):
    if cur > 0:
        res += 1
    cur = max(cur - 1, a[i])
print(n - res)
