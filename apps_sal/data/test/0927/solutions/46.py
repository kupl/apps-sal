#!/usr/bin/env python3

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))


all_weights = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
weights = [all_weights[i] for i in a]

# print(weights)

dp = [-1 for _ in range(n + 1)]
dp[0] = 0

for i in range(1, n + 1):
    # print(dp)
    for j in range(len(weights)):
        if i - weights[j] >= 0:
            dp[i] = max(dp[i - weights[j]] * 10 + a[j], dp[i])

print((dp[-1]))
