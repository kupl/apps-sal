import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, T = lr()
AB = [lr() for _ in range(N)]
AB.sort()
# 時間のかかる物は後ろへ
dp = np.zeros(T, np.int64)
answer = 0
for a, b in AB:
    answer = max(answer, dp.max() + b)
    prev = dp
    dp[a:] = np.maximum(prev[a:], prev[:-a] + b)

print(answer)
