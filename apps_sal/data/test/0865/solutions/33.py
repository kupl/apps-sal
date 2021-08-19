import sys
import numpy as np


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


(N, T) = lr()
AB = [lr() for _ in range(N)]
AB.sort()
dp = np.zeros(T, np.int32)
temp_ans = 0
for (a, b) in AB:
    temp_ans = max(temp_ans, dp.max() + b)
    dp[a:] = np.maximum(dp[a:], dp[:-a] + b)
print(temp_ans)
