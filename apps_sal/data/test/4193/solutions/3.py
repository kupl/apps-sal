a = [list(map(int, input().split())) for i in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]
bingo = []
for i in range(3):
    x = a[i]
    for j in range(3):
        bingo.append(x[j])
for i in b:
    for j in range(0, 9):
        if i == bingo[j]:
            bingo[j] = 0
if bingo[0] == 0 and bingo[1] == 0 and (bingo[2] == 0):
    print('Yes')
elif bingo[3] == 0 and bingo[4] == 0 and (bingo[5] == 0):
    print('Yes')
elif bingo[6] == 0 and bingo[7] == 0 and (bingo[8] == 0):
    print('Yes')
elif bingo[0] == 0 and bingo[3] == 0 and (bingo[6] == 0):
    print('Yes')
elif bingo[1] == 0 and bingo[4] == 0 and (bingo[7] == 0):
    print('Yes')
elif bingo[2] == 0 and bingo[5] == 0 and (bingo[8] == 0):
    print('Yes')
elif bingo[0] == 0 and bingo[4] == 0 and (bingo[8] == 0):
    print('Yes')
elif bingo[2] == 0 and bingo[4] == 0 and (bingo[6] == 0):
    print('Yes')
else:
    print('No')
