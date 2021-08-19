import sys
import math
(n, m) = map(int, input().split())
m -= 1
z = list(map(int, input().split()))
a = m
b = m
ans = 0
while a < n or b >= 0:
    if a < n and b >= 0 and (a != b):
        if z[a] == 1 and z[b] == 1:
            ans += 2
    elif a == b:
        if z[a] == 1:
            ans += 1
    elif b >= 0:
        if z[b] == 1:
            ans += 1
    elif z[a] == 1:
        ans += 1
    a += 1
    b -= 1
print(ans)
