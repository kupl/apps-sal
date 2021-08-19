#!/usr/bin/env python3

# import
#import math
#import numpy as np
N, M = list(map(int, input().split()))
A = [int(input()) for _ in range(M)]

dp = [0] * (N + 1)
dp[0] = 1

safe = []
for i in range(1, N + 1):
    if len(A) != 0:
        if A[0] == i:
            A.pop(0)
            continue

    safe.append(i)

for s in safe:
    for i in range(1, 3):
        if s - i >= 0:
            dp[s] += dp[s - i]
    dp[s] %= 10 ** 9 + 7

print((dp[N]))
