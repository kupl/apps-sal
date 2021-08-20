bingo = []
kiroku = [[0, 0, 0] for i in range(3)]
for i in range(3):
    (a, b, c) = map(int, input().split())
    bingo.append([a, b, c])
n = int(input())
for j in range(n):
    num = int(input())
    for k in range(3):
        for l in range(3):
            if bingo[k][l] == num:
                kiroku[k][l] = 1
ans = 0
for i in range(3):
    if kiroku[i][0] == kiroku[i][1] == kiroku[i][2] == 1 or kiroku[0][i] == kiroku[1][i] == kiroku[2][i] == 1:
        ans = 1
        break
if kiroku[0][0] == kiroku[1][1] == kiroku[2][2] == 1 or kiroku[0][2] == kiroku[1][1] == kiroku[2][0] == 1:
    ans = 1
if ans == 1:
    print('Yes')
else:
    print('No')
