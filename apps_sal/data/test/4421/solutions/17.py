from math import floor
from collections import defaultdict
(n, k) = map(int, input().split())
a = defaultdict(int)
for i in input().split():
    i = int(i) % k
    a[i] += 1
r = 0
for i in range(floor(k / 2) + 1):
    if i == 0 or i == k - i:
        r += a[i] // 2
    else:
        r += min(a[i], a[k - i])
print(r * 2)
