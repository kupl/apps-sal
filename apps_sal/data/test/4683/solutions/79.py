import numpy as np
import itertools as it
n = int(input())
a = list(map(int, input().split()))
_sum = 0
ans = 0
mod = 1000000007

for i in range(n):
    _sum += a[i]
    _sum %= mod

for i in range(n):
    _sum -= a[i]
    if _sum < 0:
        _sum += mod
    ans += a[i] * _sum
    ans %= mod

print(ans)
