#!/usr/bin/env python

n, k = list(map(int, input().split()))
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
for i in range(n):
    a[i], b[i] = list(map(int, input().split()))

d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = b[i]
    else:
        d[a[i]] += b[i]

d = sorted(list(d.items()), key=lambda x: x[0])

tmp = 0
for i in range(len(d)):
    tmp += d[i][1]
    if tmp >= k:
        print((d[i][0]))
        return
