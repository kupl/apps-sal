#!/usr/bin/env python3
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
delta = [0] * m
ans = []
acc = 0
for k in range(n):
    delta[k % m] += a[k]
    acc += delta[k % m]
    ans.append(acc)
print(*ans)
