import numpy as np
from bisect import bisect_right
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
b = sorted(b)
c = sorted(c)
d = []
for i in range(n):
    index = bisect_right(c, b[i])
    d.append(n - index)
s = sum(d)
cum = np.cumsum(d)
ans = 0
for j in range(n):
    dex = bisect_right(b, a[j])
    if dex == 0:
        ans += s
    elif dex == n:
        continue
    else:
        ans += s - cum[dex - 1]
print(ans)
