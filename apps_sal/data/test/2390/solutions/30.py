from itertools import *
n, c, *u = map(int, open(0).read().split())
x, a = u[::2] + [c], [0] + list(accumulate(u[1::2]))
ans = l = r = 0
for b in range(n + 1):
    t, d, l, r = a[n] - a[b], c - x[b], max(l, a[b] - x[b - 1]), max(r, a[b] - 2 * x[b - 1])
    ans = max(ans, l + t - 2 * d, r + t - d)
print(ans)
