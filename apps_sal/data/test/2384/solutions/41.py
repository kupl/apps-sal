N_all = int(input())
A = list(map(int, input().split()))
f_inf = -float('inf')
odds_or_even = N_all % 2 + 2
dp = [[f_inf for x in range(N_all + 1)] for x in range(odds_or_even)]
dp[0][0] = 0
for i in range(N_all):
    dp[0][i + 1] = dp[0][i] + A[i] * ((i + 1) % 2)
for j in range(1, odds_or_even):
    for i in range(N_all):
        dp[j][i + 1] = max(dp[j][i] + A[i] * ((i + j + 1) % 2), dp[j - 1][i])
print(dp[odds_or_even - 1][N_all])
