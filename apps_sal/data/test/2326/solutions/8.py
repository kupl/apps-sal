N = 1009
MOD = 998244353

a = [0] * N
dp = [0] * N
C = []
for i in range(0, N):
    C.append([0] * N)

for i in range(0, N):
    C[i][0] = 1
    C[i][i] = 1
    for j in range(1, i):
        C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % MOD

n = int(input())
b = input().split()
for i in range(0, n):
    a[i] = int(b[i])

dp[n] = 1
for i in range(n - 1, -1, -1):
    if(a[i] <= 0):
        continue
    for j in range(i + a[i] + 1, n + 1):
        dp[i] += (dp[j] * C[j - i - 1][a[i]]) % MOD
        dp[i] %= MOD

soma = 0
for i in range(0, n):
    soma += dp[i]
    soma %= MOD

print(soma)
