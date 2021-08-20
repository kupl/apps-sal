import numpy as np
(n, k) = list(map(int, input().split()))
a = np.array(list(map(int, input().split())))
a.sort()
(l, r) = (0, 10000000000)
while r - l > 1:
    m = (l + r) // 2
    res = n * n - a.searchsorted(m - a).sum()
    if res >= k:
        l = m
    else:
        r = m
b = np.array([0] * (n + 1))
for i in range(1, n + 1):
    b[i] = b[i - 1] + a[n - i]
cnt = 0
ans = 0
for x in a:
    t = n - a.searchsorted(l - x)
    ans += b[t] + x * t
    cnt += t
print(ans - (cnt - k) * l)
