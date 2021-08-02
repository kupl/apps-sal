#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
a.sort()
c = 0
for i in range(1, n):
    if a[i] <= a[i - 1]:
        c += a[i - 1] + 1 - a[i]
        a[i] = a[i - 1] + 1
print(c)
