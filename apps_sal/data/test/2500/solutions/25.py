n = int(input())
a = format(n, "b")
mod = 1000000007
dp = [[0 for j in range(3)] for i in range(len(a) + 1)]
dp[0][0] = 1
for i in range(len(a)):
    for j in range(3):
        for x in range(2):
            for y in range(x, 2):
                b = (n >> i) & 1
                dp[i + 1][(x + y + j - b + 1) // 2] = (dp[i + 1][(x + y + j - b + 1) // 2] + dp[i][j]) % mod
print(dp[len(a)][0])
