n = int(input())
A_l = [(A, i) for i, A in enumerate(map(int, input().split()))]
A_l.sort(reverse=True)

dp = []
for _ in range(n + 1):
    dp.append([0] * (n + 1))
for j in range(1, n + 1):
    a, i = A_l[j - 1]
    dp[j][0] = dp[j - 1][0] + a * (n - (j - 1) - (i + 1))
for k in range(1, n + 1):
    a, i = A_l[k - 1]
    dp[0][k] = dp[0][k - 1] + a * ((i + 1) - (1 + (k - 1)))

for j in range(1, n + 1):
    for k in range(1, n - j + 1):
        a, i = A_l[j + k - 1]
        j_plus = a * (n - (j - 1) - (i + 1))
        k_plus = a * ((i + 1) - (1 + (k - 1)))
        dp[j][k] = max(dp[j - 1][k] + j_plus, dp[j][k - 1] + k_plus)

result = 0
for j in range(0, n + 1):
    k = n - j
    result = max(result, dp[j][k])
print(result)
