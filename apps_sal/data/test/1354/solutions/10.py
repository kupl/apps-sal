import math
from bisect import bisect_right, bisect_left
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import accumulate

R = lambda: map(int, input().split())
mm, k, a = R()
junk = int(input())
arr = list(R())

l, r = 0, len(arr)
while l < r:
    m = (l + r) // 2
    tarr = [0] + sorted(arr[:m + 1]) + [mm + 1]
    cnt = 0
    for i in range(1, len(tarr)):
        cnt += (tarr[i] - tarr[i - 1]) // (a + 1)
    if cnt < k:
        r = m
    else:
        l = m + 1
print(l + 1 if l < len(arr) else -1)
