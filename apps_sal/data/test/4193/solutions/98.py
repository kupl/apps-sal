board = [list(map(int,input().split())) for i in range(3)]
num = int(input())
for n in range(num):
    bi = int(input())
    for i in range(3):
        for j in range(3):
            if board[i][j] == bi:
                board[i][j] = 0

#横
for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] == 0:
        print("Yes")
        return
#縦
for i in range(3):
    if board[0][i] == board[1][i] == board[2][i] == 0:
        print("Yes")
        return

if board[0][0] == board[1][1] == board[2][2] == 0:
    print("Yes")
    return
if board[0][2] == board[1][1] == board[2][0] == 0:
    print("Yes")
    return

print("No")
