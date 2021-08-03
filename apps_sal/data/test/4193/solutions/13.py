def LIHW(h):
    return [list(map(int, input().split())) for _ in range(h)]


def LIH(h):
    return [int(input()) for _ in range(h)]


card = LIHW(3)
N = int(input())
num = LIH(N)
bingo = [[0, 0, 0] for _ in range(3)]
for i in num:
    for a in range(3):
        for b in range(3):
            if i == card[a][b]:
                bingo[a][b] = 1
                break
ans = "No"
for i in range(3):
    if bingo[i][0] == 1 and bingo[i][1] == 1 and bingo[i][2] == 1:
        ans = "Yes"
for i in range(3):
    if bingo[0][i] == 1 and bingo[1][i] == 1 and bingo[2][i] == 1:
        ans = "Yes"
if bingo[0][0] == 1 and bingo[1][1] == 1 and bingo[2][2] == 1:
    ans = "Yes"
if bingo[0][2] == 1 and bingo[1][1] == 1 and bingo[2][0] == 1:
    ans = "Yes"
print(ans)
