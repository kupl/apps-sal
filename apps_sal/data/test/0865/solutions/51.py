import numpy as np
(N, T) = map(int, input().split())
dp = np.zeros(T, dtype=int)
maxval = 0
meals = [None] * N
for i in range(N):
    (a, b) = map(int, input().split())
    meals[i] = (a, b)
meals = sorted(meals, key=lambda x: x[0])
for i in range(N):
    (a, b) = meals[i]
    if maxval < dp[-1] + b:
        maxval = dp[-1] + b
    np.maximum(dp[:-a] + b, dp[a:], out=dp[a:])
print(maxval)
