#!/usr/bin/env python

n, k = list(map(int, input().split()))

# aは全探索
ans = 0
for a in range(1, n + 1):
    ra = a % k
    rbc = k - ra
    if (2 * rbc) % k == 0:
        ans += ((n - rbc) // k + 1)**2

print(ans)
