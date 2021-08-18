import numpy as np

N, T = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort()
dp = np.zeros(T, dtype=np.int32)
temp_ans = 0
for a, b in AB:
    temp_ans = max(temp_ans, dp.max() + b)
    dp[a:] = np.maximum(dp[a:], dp[:-a] + b)
print(temp_ans)
