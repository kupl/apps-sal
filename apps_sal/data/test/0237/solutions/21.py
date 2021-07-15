import sys
import math

n, m, k = map(int, input().split())

ans = 1
m -= n
l = min(k - 1, n - k)
step = 1

for i in range(l):
    if m - step < 0:
        print(ans)
        return

    m -= step
    step += 2
    ans += 1

while step < n:
    if m - step < 0:
        print(ans)
        return

    m -= step
    step += 1
    ans += 1

ans += m // n

print(ans)
