n = int(input())
dp = [[0] * 64 for _ in [0] * n]
mod = 10 ** 9 + 7
A = 0
C = 1
G = 2
T = 3
AGC = 16 * A + 4 * G + C
ACG = 16 * A + 4 * C + G
GAC = 16 * G + 4 * A + C
for j in range(64):
    if j == AGC or j == ACG or j == GAC:
        dp[2][j] = 0
    else:
        dp[2][j] = 1
for i in range(3, n):
    tot = [sum(dp[i - 1][k::16]) for k in range(16)]
    for j in range(64):
        c1 = j // 16
        c2 = j // 4 % 4
        c3 = j % 4
        d = tot[j // 4]
        if j == AGC or j == ACG or j == GAC:
            d = 0
        elif c2 == G and c3 == C:
            d -= dp[i - 1][c1 * 4 + G]
        elif c1 == G and c3 == C:
            d -= dp[i - 1][G * 4 + c2]
        dp[i][j] = d % mod
print(sum(dp[-1]) % mod)
