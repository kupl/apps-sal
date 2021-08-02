#!/usr/bin/env python3
from collections import deque
import sys
sys.setrecursionlimit(10**6)


k = int(input())
q = deque()
q.append(1)

dp = [10**10] * (k)
dp[1] = 0

while q:
    u = q.popleft()
    if dp[(u * 10) % k] > dp[u]:
        dp[(u * 10) % k] = dp[u]
        q.appendleft((u * 10) % k)
    if dp[(u + 1) % k] > dp[u] + 1:
        dp[(u + 1) % k] = dp[u] + 1
        q.append((u + 1) % k)

print((dp[0] + 1))
