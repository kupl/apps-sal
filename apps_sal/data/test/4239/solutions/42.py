import numpy as np

def chmin(dp, i, a):
    if dp[i] < a:
        return
    else:
        dp[i] = a
        return

N = int(input())

dp = np.array([i for i in range(N+1)]) # 1円ずつ引き出したときの回数で初期化

for i in range(N+1):
    x = 1
    while i + 6**x <= N:
        chmin(dp, i + 6**x, dp[i]+1)
        if i + 9**x <= N:
            chmin(dp, i + 9**x, dp[i]+1)
        x += 1

print(dp[N])
