#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))

l = a[0]
r = sum(a) - l
ans = abs(l - r)

for i in range(1, n - 1):
    l += a[i]
    r -= a[i]
    if abs(l - r) <= ans:
        ans = abs(l - r)

print(ans)
