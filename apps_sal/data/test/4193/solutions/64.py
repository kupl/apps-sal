def bingo(board):
    if board[0][0] == board[0][1] == board[0][2]:
        return True
    if board[1][0] == board[1][1] == board[1][2]:
        return True
    if board[2][0] == board[2][1] == board[2][2]:
        return True
    if board[0][0] == board[1][0] == board[2][0]:
        return True
    if board[0][1] == board[1][1] == board[2][1]:
        return True
    if board[0][2] == board[1][2] == board[2][2]:
        return True
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[0][2]:
        return True


A = []
b = []
for _ in range(3):
    A.append(list(map(int, input().split())))
n = int(input())
for _ in range(n):
    b.append(int(input()))

for i in range(n):
    for j in range(3):
        for k in range(3):
            if b[i] == A[j][k]:
                A[j][k] = 0

ans = bingo(A)
if ans:
    print('Yes')
else:
    print('No')
