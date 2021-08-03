import heapq
from bisect import bisect_left, bisect_right
from collections import Counter
from collections import OrderedDict
from collections import deque
from itertools import accumulate, product

import math


def R(): return map(int, input().split())


n = int(input())
snows = list(R())
melts = list(R())
acc = list(accumulate(melts))
cnt, rem = [0] * n, [0] * n
for i, s in enumerate(snows):
    ri = bisect_right(acc, s + (acc[i - 1] if i > 0 else 0))
    cnt[i] += 1
    if ri < n:
        cnt[ri] -= 1
        rem[ri] += s + (acc[i - 1] if i > 0 else 0) - (acc[ri - 1] if ri > 0 else 0)
cnt = list(accumulate(cnt))
for i in range(n):
    print(melts[i] * cnt[i] + rem[i], end=' ')
