
import sys
from functools import lru_cache
n, m = [int(x) for x in input().split()]


res = 0
while n < m:
    res += 1
    if m % 2 == 0:
        m //= 2
    else:
        m += 1

res += (n - m)

print(res)
