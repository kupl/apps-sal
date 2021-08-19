#!/usr/bin/env python

n = int(input())
p = list(map(int, input().split()))

dup = []
for i in range(n):
    if i + 1 == p[i]:
        dup.append(0)
    else:
        dup.append(1)

ans = 0
i = 0
while i < n - 1:
    if dup[i] == dup[i + 1] == 0:
        ans += 1
        i += 2
    elif dup[i] == 0 and dup[i + 1] == 1:
        ans += 1
        i += 2
    else:
        i += 1

if i == n - 1:
    if dup[-1] == 0:
        ans += 1

print(ans)
