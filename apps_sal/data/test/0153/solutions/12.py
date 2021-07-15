from itertools import accumulate
from bisect import *
n, k, m = list(map(int, input().split()))
t = sorted(map(int, input().split()))

res = 0
s = sum(t)
ps = list(accumulate(t))
for x in range(min(n, m//s)+1):
    rem = m - x*s
    if x < n:
        y = bisect_right(ps, rem/(n-x))
        rem -= (n-x)*(ps[y-1] if y>0 else 0)
        if y < k:
            z = rem // t[y]
        else:
            z = 0
    else:
        y = z = 0
    r = x*(k+1) + y*(n-x) + z + ((n-x) if y==k else 0) + (z if y == k-1 else 0)
    res = max(res, r)
print(res)
