import bisect

import sys
stdin = sys.stdin


def ip(): return int(sp())
def fp(): return float(sp())
def lp(): return list(map(int, stdin.readline().split()))
def sp(): return stdin.readline().rstrip()
def yp(): return print('Yes')
def np(): return print('No')


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
