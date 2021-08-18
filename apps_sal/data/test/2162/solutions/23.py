k1, k2, k3 = map(int, input().split())
s = [set([int(o) for o in input().split()]) for i in range(3)]
n = k1 + k2 + k3
dp = [[float('inf')] * 3 for i in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(3):
        for k in range(j, 3):
            dp[i][k] = min(dp[i][k], dp[i - 1][j] + (i not in s[k]))

print(min(dp[n]))
