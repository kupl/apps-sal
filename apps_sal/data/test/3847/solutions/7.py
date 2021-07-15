from itertools import accumulate
from sys import stdout

R = lambda: map(int, input().split())
n, m = R()
a, b = list(accumulate(R())), list(R())
x = int(input())
res = 0
for al in range(1, n + 1):
    sa = min(ar - al for ar, al in zip(a[al - 1:], [0] + a[:]))
    l, s = -1, 0
    for r in range(m):
        s += b[r] * sa
        while s > x:
            l += 1
            s -= b[l] * sa
        res = max(res, al * (r - l))
print(res)
