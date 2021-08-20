import sys
(n, k) = map(int, input().split())
k -= 1
(lo, hi) = (0, int(1000000000.0))
while lo < hi:
    m = (lo + hi + 1) // 2
    if 1 + k * (k + 1) // 2 - m * (m + 1) // 2 >= n:
        lo = m
    else:
        hi = m - 1
if 1 + k * (k + 1) // 2 - lo * (lo + 1) // 2 >= n:
    lo = k - lo
else:
    lo = -1
print(lo)
