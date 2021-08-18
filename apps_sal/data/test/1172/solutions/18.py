import sys
readline = sys.stdin.readline

S = readline().rstrip()
DIV = 10 ** 9 + 7

dp = [[0] * 4 for i in range(len(S) + 1)]

dp[0][0] = 1

for i in range(len(S)):
    for j in range(4):
        dp[i + 1][j] += dp[i][j] * (3 if S[i] == "?" else 1)

    if S[i] == "A" or S[i] == "?":
        dp[i + 1][1] += dp[i][0]

    if S[i] == "B" or S[i] == "?":
        dp[i + 1][2] += dp[i][1]

    if S[i] == "C" or S[i] == "?":
        dp[i + 1][3] += dp[i][2]

    for j in range(4):
        dp[i + 1][j] %= DIV

print((dp[len(S)][3]))
