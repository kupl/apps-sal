sheet = []
for i in range(3):
    sheet.append([int(x) for x in input().split()])
bingo = [[False] * 3 for _ in range(3)]

N = int(input())
for i in range(N):
    a = int(input())
    for x in range(3):
        for y in range(3):
            if sheet[x][y] == a:
                bingo[x][y] = True

for i in range(3):
    if bingo[i][0] and bingo[i][1] and bingo[i][2]:
        print('Yes')
        return
    if bingo[0][i] and bingo[1][i] and bingo[2][i]:
        print('Yes')
        return
if bingo[0][0] and bingo[1][1] and bingo[2][2]:
    print('Yes')
    return
if bingo[2][0] and bingo[1][1] and bingo[0][2]:
    print('Yes')
    return

print('No')

