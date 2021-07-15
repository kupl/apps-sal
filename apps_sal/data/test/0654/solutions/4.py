n = int(input())

board = [[0 for i in range(n + 1)] for j in range(2 * n + 1)]

board[0][0] = 1
for i in range(1, n):
    for j in range(len(board[0])):
        if j > 0:
            board[i][j-1] += board[i-1][j]
        if j + 1 < len(board[0]) and j < 2 * n - i:
            board[i][j+1] += board[i-1][j]
for i in range(n, 2 * n + 1):
    for j in range(len(board[0])):
        if j > 0:
            board[i][j-1] += board[i-1][j]
            #board[i][j-1] %= 1000000007
        if j + 1 < len(board[0]) and j < 2 * n - i:
            board[i][j+1] += board[i-1][j]       
            #board[i][j+1] %= 1000000007     
ans = 0
for i in range(1, len(board), 2):
    
    ans += sum(board[i])
    ans %= 1000000007
        
print(ans)
