import heapq
from bisect import bisect_left, bisect_right, insort
from collections import Counter
from collections import OrderedDict
from collections import deque
from itertools import accumulate, product

import math


def R(): return map(int, input().split())


s = input()
l, r, z = 0, 0, [0] * len(s)
for i in range(1, len(s)):
    if i > r - 1:
        l = r = i
        while r < len(s) and s[r] == s[r - i]:
            r += 1
        z[i] = r - l
    elif z[i - l] < r - i:
        z[i] = z[i - l]
    else:
        l = i
        while r < len(s) and s[r] == s[r - i]:
            r += 1
        z[i] = r - l
sz = sorted(z[:])
res = []
for i in range(len(s) - 1, 0, -1):
    if z[i] == len(s) - i:
        res.append((z[i], len(sz) - bisect_left(sz, z[i])))
print(len(res) + 1)
for x in res:
    print(x[0], x[1] + 1)
print(len(s), 1)
