#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]

total = 0
for i in range(n + 1):
    total += abs(a[i] - a[i + 1])

for i in range(1, n + 1):
    ans = total - (abs(a[i] - a[i - 1]) + abs(a[i + 1] - a[i])) + abs(a[i + 1] - a[i - 1])
    print(ans)
