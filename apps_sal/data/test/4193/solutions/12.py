def ck_bingo(lis):
    flg = False
    for i in range(0, 3):
        if lis[i][0] + lis[i][1] + lis[i][2] == 3:
            flg = True
            break
    for j in range(0, 3):
        if lis[0][j] + lis[1][j] + lis[2][j] == 3:
            flg = True
            break
    if lis[0][0] + lis[1][1] + lis[2][2] == 3 or lis[0][2] + lis[1][1] + lis[2][0] == 3:
        flg = True
    return flg


Bingo = [[0] for _ in range(3)]
for b in range(3):
    Bingo[b] = list(map(int, input().split()))
N = int(input())
A = [[0, 0, 0] for _ in range(3)]
Ans = 'No'
for i in range(N):
    ball = int(input())
    for j in range(3):
        for k in range(3):
            if ball == Bingo[j][k]:
                A[j][k] = 1
                if ck_bingo(A):
                    Ans = 'Yes'
print(Ans)
