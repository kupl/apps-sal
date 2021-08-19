#!/usr/bin/env python

n, k = list(map(int, input().split()))

if k % 2 == 1:
    ans = (n // k)**3
else:
    ans = (n // k)**3 + (((n - (k // 2)) // k) + 1)**3

print(ans)
