#!/usr/bin/env python3

N = int(input())
K = int(input())

ans = 1
for i in range(N):
    a = ans * 2
    b = ans + K
    ans = min(a, b)
print(ans)
