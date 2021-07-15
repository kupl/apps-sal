from math import *

n, a, b, k = list(map(int, input().split()))
h = [int(i) for i in input().split()]

ans = n
nh = []
for m in h:
    tr = max(0, (m - 1) // (a+b))
    m -= tr*(a+b)
    m -= a
    if m > 0:
        nh.append(m)
        ans -= 1

nh.sort()
i = 0
while k > 0 and i < len(nh):
    k -= ceil(nh[i]/a)
    if k < 0:
        break
    i += 1
    ans += 1

print(ans)

