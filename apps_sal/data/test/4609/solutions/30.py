#!/usr/bin/env python

n = int(input())
a = [int(input()) for _ in range(n)]

d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1 
    else:
        d[a[i]] += 1

ans = 0 
for s in list(d.values()):
    if s%2 == 1:
        ans += 1

print(ans)

