from math import *
T = int(input())
for kase in range(T):
    (n, d) = [int(x) for x in input().split()]
    m = ceil(sqrt(d))
    (l, r) = (m - 10, m + 10)
    l = max(0, l)
    ans = 1e+100
    for x in range(l, r):
        ans = min(ans, x + ceil(d / (x + 1)))
    if ans <= n:
        print('YES')
    else:
        print('NO')
