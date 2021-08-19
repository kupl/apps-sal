#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
ma = a[-1]
div = [0 for _ in range(ma + 1)]

for i in range(n):
    for j in range(a[i], ma + 1, a[i]):
        div[j] += 1

ans = 0
for i in range(n):
    if div[a[i]] == 1:
        ans += 1
print(ans)
