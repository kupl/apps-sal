import sys
input = sys.stdin.readline
import numpy as np
from collections import defaultdict

# 最後に置いたものは赤とする（3倍）
# 青、緑を最後にいつ置いたのかを持ってdp

MOD = 10 ** 9 + 7
N,M = map(int,input().split())
LRX = [[int(x) for x in input().split()] for _ in range(M)]

R_to_LX = defaultdict(list)
for l,r,x in LRX:
    R_to_LX[r].append((l,x))

# 1個目を置いた時点
for n in range(1,N+1):
    if n == 1:
        dp = np.zeros((n,n), dtype = np.int64)
        dp[0,0] = 1
    else:
        prev = dp
        dp = np.zeros((n,n), dtype = np.int64)
        # 同色
        dp[:-1,:-1] = prev
        # 青から赤に
        dp[n-1,:-1] = prev.sum(axis = 0)
        # 緑から赤に
        dp[:-1,n-1] = prev.sum(axis = 1)
    # ルール違反を除外する
    for l,x in R_to_LX[n]:
        if x == 1:
            dp[l:,:] = 0
            dp[:,l:] = 0
        elif x == 2:
            dp[l:,l:] = 0
            dp[:l,:l] = 0
        elif x == 3:
            dp[:l,:] = 0
            dp[:,:l] = 0
    dp %= MOD

answer = dp.sum() * 3 % MOD
print(answer)
