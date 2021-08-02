from itertools import accumulate
from bisect import *
n, k, m = list(map(int, input().split()))
t = sorted(map(int, input().split()))

res = 0
for x in range(min(n, m // sum(t)) + 1):
    mm = m - x * sum(t); r = x * (k + 1)
    for i, ti in enumerate(t):
        for _ in range(n - x):
            if mm >= ti:
                mm -= ti
                r += 1 if i < k - 1 else 2
    res = max(res, r)
print(res)
