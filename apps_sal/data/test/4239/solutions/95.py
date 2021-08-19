N = int(input())

# dp[i] := i円引き出すのに必要な最小操作回数
dp = [float('inf')] * (N + 1)
dp[0] = 0
operates = sorted([1, 6, 36, 216, 1296, 7776, 46656, 9, 81, 729, 6561, 59049])
for i in range(N):
    for ope in operates:
        if i + ope > N:
            break
        dp[i + ope] = min(dp[i + ope], dp[i] + 1)

print((dp[N]))
