#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))

d = {}
cnt = 0
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1

for key in list(d.keys()):
    if d[key] != key:
        if d[key] < key:
            cnt += d[key]
        else:
            cnt += d[key] - key

print(cnt)
