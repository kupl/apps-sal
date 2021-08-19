S = int(input())
MOD = 10 ** 9 + 7
DP = [0] * 2001
DP[0] = 1
for i in range(3, S + 1):
    DP[i] = DP[i - 1] + DP[i - 3]
    DP[i] %= MOD
print(DP[S])
