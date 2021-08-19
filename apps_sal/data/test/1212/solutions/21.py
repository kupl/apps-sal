minimum = pow(10, 19)
index = 0
(n, k) = list(map(int, input().split(' ')))
fence = list(map(int, input().split(' ')))
dp = [0] + [fence[0]] + [0] * (n - 1)
for t in range(2, n + 1):
    dp[t] = dp[t - 1] + fence[t - 1]
for u in range(n - k + 1):
    value = dp[u + k] - dp[u]
    if value < minimum:
        index = u
        minimum = value
print(index + 1)
