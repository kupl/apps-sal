(n, m) = map(int, input().split())
a = [int(i) for i in input().split()]
match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in a:
        if i - match[j] < 0:
            continue
        if dp[i - match[j]] == -1:
            continue
        dp[i] = max(dp[i], dp[i - match[j]] * 10 + j)
print(dp[n])
