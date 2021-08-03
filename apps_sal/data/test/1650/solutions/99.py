L = list(input())
L = list(map(int, L))
dp = [2, 1]
MOD = 10**9 + 7
for j in range(1, len(L)):
    a, b = dp
    if L[j] == 1:
        dp[0] = (a * 2) % MOD
        dp[1] = (a + b * 3) % MOD
    elif L[j] == 0:
        dp[1] = (b * 3) % MOD
print(sum(dp) % MOD)
