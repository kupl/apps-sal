board = []
board.append(input())
board.append(input())

n = len(board[0])

dp = [[0 for _ in range(n)] for _ in range(4)]

inf = float('-inf')

if board[0][0] == 'X':
    dp[0][0] = inf
    dp[2][0] = inf
if board[1][0] == 'X':
    dp[0][0] = inf
    dp[1][0] = inf


#print([dp[j][0] for j in range(4)])
for i in range(1, n):
    prev_best = max(dp[j][i - 1] for j in range(4))
    for j in range(4):
        dp[j][i] = prev_best
    if board[0][i] != 'X' or board[1][i] != 'X':
        dp[3][i] = max(dp[3][i], dp[0][i - 1] + 1)
    if board[0][i] != 'X' and board[1][i] != 'X':
        dp[1][i] = max(dp[1][i], dp[0][i - 1] + 1)
        dp[2][i] = max(dp[2][i], dp[0][i - 1] + 1)
        dp[3][i] = max(dp[3][i], dp[1][i - 1] + 1, dp[2][i - 1] + 1)
    if board[0][i] == 'X':
        dp[0][i] = inf
        dp[2][i] = inf
    if board[1][i] == 'X':
        dp[0][i] = inf
        dp[1][i] = inf
    #print([dp[j][i] for j in range(4)])

print(max(max(dp[i][-1] for i in range(4)), 0))
