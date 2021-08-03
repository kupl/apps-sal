from itertools import accumulate
from collections import defaultdict
import bisect

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a = [0] + list(accumulate([(i - 1) % k for i in a]))
a = [i % k for i in a]
ans = 0
maps = defaultdict(list)
for k1, v in enumerate(a):
    maps[v].append(k1)
for i in range(n):
    v = a[i]
    ans += bisect.bisect_right(maps[v], i + k - 1) - bisect.bisect_right(maps[v], i)
print(ans)
