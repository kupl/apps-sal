import itertools as it
import math
import functools as ft
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
res = 100000
for i in a:
    if k % i == 0:
        res = min(res, k // i)
print(res)
