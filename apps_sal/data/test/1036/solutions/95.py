win = {'R': 'P', 'P': 'S', 'S': 'R'}
n, k = list(map(int, input().split()))
dp = [[c for c in input()]]
for i in range(k):
    dp.append([*dp[i]])
    for j in range(n):
        a = dp[i][(j * 2) % n]
        b = dp[i][(j * 2 + 1) % n]
        dp[i + 1][j] = b if win[a] == b else a
print((dp[k][0]))
