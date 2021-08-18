A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
sheet = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(N):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if b == A[j][k]:
                sheet[j][k] = 1
                break
            else:
                continue

for i in range(3):
    if sheet[0][i] == sheet[1][i] == sheet[2][i] == 1:
        print('Yes')
        return

for i in range(3):
    if sheet[i][0] == sheet[i][1] == sheet[i][2] == 1:
        print('Yes')
        return

if sheet[0][0] == sheet[1][1] == sheet[2][2] == 1:
    print('Yes')
    return
if sheet[0][2] == sheet[1][1] == sheet[2][0] == 1:
    print('Yes')
    return
else:
    print('No')
