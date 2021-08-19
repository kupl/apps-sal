import sys
import bisect
import math
from itertools import permutations
m = 1000000007


def find_lt(a, x):
    """Find rightmost value less than x"""
    i = bisect.bisect_left(a, x)
    if i:
        return a[i - 1]
    else:
        return -1


n = int(input())
ans = 0
for i in range(1, n):
    if (n - i) % i == 0:
        ans += 1
print(ans)
