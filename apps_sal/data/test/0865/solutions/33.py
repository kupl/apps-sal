import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, T = lr()
AB = [lr() for _ in range(N)]
AB.sort()
# 最後の注文はAiが選ぶ料理で最大で、T-1分後に注文するとして良い
dp = np.zeros(T, np.int32)
temp_ans = 0
for a, b in AB:
    temp_ans = max(temp_ans, dp.max()+b)
    dp[a:] = np.maximum(dp[a:], dp[:-a]+b)

print(temp_ans)

