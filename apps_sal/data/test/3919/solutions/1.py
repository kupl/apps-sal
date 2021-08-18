import numpy as np
import sys
input = sys.stdin.readline


MOD = 10**9 + 7

N, M = map(int, input().split())
S = np.array(list(input().rstrip()), dtype='U1')
LR = [[int(x) for x in input().split()] for _ in range(M)]

cnt_0 = (S == '0').cumsum()
cnt_1 = (S == '1').cumsum()
canuse_0 = cnt_0
canuse_1 = cnt_1
for L, R in LR:
    canuse_0[L - 1] = max(canuse_0[L - 1], cnt_0[R - 1])
    canuse_1[L - 1] = max(canuse_1[L - 1], cnt_1[R - 1])
np.maximum.accumulate(canuse_0, out=canuse_0)
np.maximum.accumulate(canuse_1, out=canuse_1)

dp = np.zeros(N + 1, dtype=np.int64)
dp[0] = 1
for i in range(N):
    prev = dp
    dp = np.zeros(N + 1, dtype=np.int64)
    left = max(0, (i + 1) - canuse_0[i])
    right = canuse_1[i]
    dp[left:right + 1] += prev[left:right + 1]
    left = max(1, left)
    dp[left:right + 1] += prev[left - 1:right]
    dp %= MOD

answer = dp.sum()
print(answer)
