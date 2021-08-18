from sys import stdin
import math

n, k = map(int, stdin.readline().split())
a = [int(x) for x in stdin.readline().split()]
nxt = [-1] * n
pref = []
f, s = -1, 0
for i in range(n):
    s += a[i]
    pref.append(s)
    nxt[n - 1 - i] = f
    if a[n - 1 - i] != 1:
        f = n - 1 - i
ans = 0
for i in range(n):
    pos, cur = i, 0
    prod = 1
    while 1:
        if prod > 1e18:
            break
        prod *= a[pos]
        cur += a[pos]
        if prod == k * cur:
            ans += 1
        nt = nxt[pos]
        if nt == -1:
            ones = n - 1 - pos
            if k * cur < prod and k * (cur + ones) >= prod:
                ans += 1
            break
        ones = nt - pos - 1
        if k * cur < prod and k * (cur + ones) >= prod and prod % k == 0:
            ans += 1
        cur += ones
        pos = nt
print(ans)
