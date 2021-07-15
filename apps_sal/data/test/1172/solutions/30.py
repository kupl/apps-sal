import sys
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

S = list(input())
N = len(S)

count = 0
DP = [[0] *  (N + 1) for _ in range(3)]
for i in range(1, N + 1):
    s = S[i - 1]
    if s == 'A':
        DP[0][i] = (DP[0][i - 1] + pow(3, count, MOD)) % MOD
        DP[1][i] = DP[1][i - 1]
        DP[2][i] = DP[2][i - 1]
    elif s == 'B':
        DP[0][i] = DP[0][i -1]
        DP[1][i] = (DP[1][i - 1] + DP[0][i - 1]) % MOD
        DP[2][i] = DP[2][i - 1]
    elif s == 'C':
        DP[0][i] = DP[0][i - 1]
        DP[1][i] = DP[1][i - 1]
        DP[2][i] = (DP[2][i - 1] + DP[1][i - 1]) % MOD
    else:
        DP[0][i] = (3 * DP[0][i - 1] + pow(3, count, MOD)) % MOD
        DP[1][i] = (3 * DP[1][i - 1] + DP[0][i - 1]) % MOD
        DP[2][i] = (3 * DP[2][i - 1] + DP[1][i - 1]) % MOD
        count += 1

print((DP[2][N]))

# print (DP)

