import heapq
from bisect import bisect_left, bisect_right
from collections import Counter
from collections import OrderedDict
from collections import deque
from itertools import accumulate, product

import math


def R(): return map(int, input().split())


n, u = R()
arr = list(R())
res = -1
for l in range(n):
    r = bisect_right(arr, arr[l] + u) - 1
    if r - l > 1:
        res = max(res, (arr[r] - arr[l + 1]) / (arr[r] - arr[l]))
print(res)
