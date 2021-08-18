import math
import itertools
from collections import deque
from collections import Counter
import heapq
import bisect
n = int(input())
d = []
a = (int(input())) * -1
d.append(a)
ans = 1
for i in range(n - 1):
    a = -1 * (int(input()))
    ind = bisect.bisect_right(d, a)
    l = len(d)
    if ind == l:
        d.append(a)
        ans += 1
    else:
        d[ind] = a
print(ans)
