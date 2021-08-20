import math
import collections
import bisect
import heapq
import time
import random
'\ncreated by shhuan at 2017/10/12 22:12\n\n'
n = int(input())
s = input()
ones = [0] * (n + 1)
for i in range(1, n + 1):
    ones[i] = ones[i - 1]
    ones[i] += s[i - 1] == '1'
ones = [2 * x for x in ones]
ones = [(x - i, i) for (i, x) in enumerate(ones)]
ds = collections.defaultdict(list)
for (d, i) in ones:
    ds[d].append(i)
ans = 0
for (k, v) in list(ds.items()):
    ans = max(ans, max(v) - min(v))
print(ans)
