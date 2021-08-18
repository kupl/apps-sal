import numpy as np

N, T = list(map(int, input().split()))
AB = [tuple(map(int, input().split())) for _ in range(N)]

AB.sort()

ans = 0
dp = [0] * T
dp = np.zeros(T, int)

for a, b in AB:
    ans = max(ans, dp[-1] + b)
    dp[a:] = np.maximum(dp[a:], dp[:-a] + b)

print(ans)
