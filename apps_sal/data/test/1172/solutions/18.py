import sys
readline = sys.stdin.readline

S = readline().rstrip()
DIV = 10 ** 9 + 7

dp = [[0] * 4 for i in range(len(S) + 1)]
# dp[i + 1][0] : i文字目まで見たとき、ABCの部分文字列がまだ始まっていない場合の数
# dp[i + 1][1] : i文字目まで見たとき、ABCのAまで一致した場合の数
# dp[i + 1][2] : i文字目まで見たとき、ABCのBまで一致した場合の数
# dp[i + 1][3] : i文字目まで見たとき、ABCのCまで一致した場合の数

dp[0][0] = 1

for i in range(len(S)):
    # 状態を遷移しない場合
    for j in range(4):
        dp[i + 1][j] += dp[i][j] * (3 if S[i] == "?" else 1)  # ?の場合は全ての遷移があり得る

    if S[i] == "A" or S[i] == "?":
        dp[i + 1][1] += dp[i][0]  # 開始状態に遷移することが出来る

    if S[i] == "B" or S[i] == "?":
        dp[i + 1][2] += dp[i][1]  # Bを使用した状態に遷移

    if S[i] == "C" or S[i] == "?":
        dp[i + 1][3] += dp[i][2]  # Cを使用した状態に遷移

    for j in range(4):
        dp[i + 1][j] %= DIV

# 最後の文字まで見たとき、Cまで一致した場合の数が答え
print((dp[len(S)][3]))
