n, k = map(int, input().split())
S = input()


def battle(h1, h2):
    return h1 if h2 + h1 in 'SRPS' else h2


dp = [[0] * n for _ in range(k + 1)]
dp[0] = list(S[:])
for i in range(1, k + 1):
    for j in range(n):
        dp[i][j] = battle(dp[i - 1][j], dp[i - 1][(j + pow(2, i - 1)) % n])
print(dp[k][0])
