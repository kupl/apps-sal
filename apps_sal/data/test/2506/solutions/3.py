from bisect import bisect_left, bisect_right
from itertools import accumulate


def ge_m(x, m, n):
    total = 0
    for v in a:
        delta = x - v
        idx = bisect_left(a, delta)
        total += n - idx
    return total >= m


(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cum = [0] + list(accumulate(a))
l = 0
r = a[-1] * 2 + 1
while r - l > 1:
    mid = (l + r) // 2
    if ge_m(mid, m, n):
        l = mid
    else:
        r = mid
num = 0
ans = 0
for v in a:
    idx = bisect_right(a, l - v)
    num += n - idx
    ans += v * (n - idx) + (cum[-1] - cum[idx])
ans += l * (m - num)
print(ans)
