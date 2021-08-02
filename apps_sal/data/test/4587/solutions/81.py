import bisect

import sys
stdin = sys.stdin

ip = lambda: int(sp())
fp = lambda: float(sp())
lp = lambda: list(map(int, stdin.readline().split()))
sp = lambda: stdin.readline().rstrip()
yp = lambda: print('Yes')
np = lambda: print('No')

n = ip()
a = lp()
b = lp()
c = lp()

a.sort()
b.sort()
c.sort()
ans = 0

for i in range(n):
    x = bisect.bisect_left(a, b[i])
    y = bisect.bisect_right(c, b[i])
    ans += x * (n - y)

print(ans)
