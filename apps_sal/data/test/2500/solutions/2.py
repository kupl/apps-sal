MOD = 10**9+7

n = int(input())
s = bin(n)[2:]
l = len(s)
dp = [[0]*4 for i in range(l+1)]
dp[0][0] = 1

for i in range(l):
    b = 1 if s[i] == '1' else 0
    for j in range(4):
        for k in range(3):
            lj = min((j<<1) + b - k, 3)
            if 0 <= lj:
                dp[i+1][lj] += dp[i][j]
                dp[i+1][lj] %= MOD

# print(dp)
print((sum(dp[l])%MOD))

