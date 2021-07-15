#!/usr/bin/env python3

n, m = list(map(int, input().split()))

ans = 1
num = int(m**0.5)+1

for i in range(1, num):
    if m % i != 0:
        continue
    j = m//i
    if i >= n:
        ans = max(ans, j)
    if j >= n:
        ans = max(ans, i)
print(ans)

