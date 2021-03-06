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
dp = np.zeros(T, np.int64)
answer = 0
for (a, b) in AB:
    answer = max(answer, dp.max() + b)
    prev = dp
    dp[a:] = np.maximum(prev[a:], prev[:-a] + b)
print(answer)
