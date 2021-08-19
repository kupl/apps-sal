#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))

ans = 1000100
ch = 0
for ch in range(min(a), max(a) + 1):
    tmp = 0
    for i in range(n):
        tmp += (a[i] - ch)**2
    if tmp <= ans:
        ans = tmp
print(ans)
