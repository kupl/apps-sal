S = input()

dp = [[0] * 4 for _ in range(len(S) + 1)]
dp[0][0] = 1
W = 'ABC'

MOD = 10 ** 9 + 7


def update1(i):
    for j in range(4):
        dp[i + 1][j] += dp[i][j] % MOD


def update2(i, c):
    ic = W.index(c)
    dp[i + 1][ic + 1] += dp[i][ic] % MOD


for i in range(len(S)):
    if S[i] == '?':
        for c in W:
            update1(i)
            update2(i, c)
    else:
        update1(i)
        update2(i, S[i])
print((dp[len(S)][-1] % MOD))

