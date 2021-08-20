n = int(input())
A = []
for i in range(n):
    x = input()
    A.append(x)
dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
mod = 10 ** 9 + 7
for i in range(n + 1):
    dp[n - 1][i] = 1
for line in range(n - 2, -1, -1):
    sum = 0
    if A[line] == 's':
        for indent in range(n):
            sum = (sum + dp[line + 1][indent]) % mod
            dp[line][indent] = sum
    else:
        for indent in range(n):
            dp[line][indent] = dp[line + 1][indent + 1]
print(dp[0][0])
