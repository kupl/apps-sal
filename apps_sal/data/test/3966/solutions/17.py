#!/usr/bin/env python
# encoding: utf-8

n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n - 1):
    ans = ans + (i + 2) * a[i]
ans = ans + n * a[n - 1]
print(ans)

