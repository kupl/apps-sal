#!/usr/bin/env python3
N = int(input())

ans = 0
for i in range(1, 10**5):
    n = i ** 2
    if n <= N:
        ans = n
    else:
        break
print(ans)
