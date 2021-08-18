from itertools import accumulate
from bisect import *
n = int(input())
a = list(map(int, input().split()))

a = [0] + list(accumulate(a))
ans = 10**18
for i in range(2, n):
    b = []
    m = a[i]
    l = bisect_right(a, m / 2)
    if abs(a[l] - m / 2) <= abs(a[l - 1] - m / 2):
        b.append(a[l])
        b.append(m - a[l])
    else:
        b.append(a[l - 1])
        b.append(m - a[l - 1])
    r = bisect_left(a, (a[-1] + m) / 2)
    if abs(a[r] - (a[-1] + m) / 2) <= abs(a[r - 1] - (a[-1] + m) / 2):
        b.append(a[r] - m)
        b.append(a[-1] - a[r])
    else:
        b.append(a[r - 1] - m)
        b.append(a[-1] - a[r - 1])

    ans = min(ans, max(b) - min(b))

print(ans)
