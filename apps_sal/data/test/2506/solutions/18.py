from itertools import accumulate
from bisect import bisect_left

n, m = list(map(int, input().split()))
a = sorted(map(int, input().split()))
cs = [0] + list(accumulate(a))
c = 0
s = 0


def f(x):
    nonlocal c, s
    c = 0
    s = 0
    for i in range(n):
        left = bisect_left(a, x - a[i])
        c += n - left
        s += cs[n] - cs[left] + (n - left) * a[i]
    return c


ok = 0
ng = 2 * 10 ** 5 + 1
while abs(ok - ng) > 1:
    x = (ok + ng) // 2
    if f(x) >= m:
        ok = x
    else:
        ng = x

print((s - (c - m) * ok))

