rows = []
for _ in range(3):
    A = list(map(int, input().split()))
    rows.append(A)
N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if rows[i][j] == b:
                rows[i][j] = 0
if rows[0][0] + rows[0][1] + rows[0][2] == 0 or rows[1][0] + rows[1][1] + rows[1][2] == 0 or rows[2][0] + rows[2][1] + rows[2][2] == 0 or (rows[0][0] + rows[1][0] + rows[2][0] == 0) or (rows[0][1] + rows[1][1] + rows[2][1] == 0) or (rows[0][2] + rows[1][2] + rows[2][2] == 0) or (rows[0][0] + rows[1][1] + rows[2][2] == 0) or (rows[0][2] + rows[1][1] + rows[2][0] == 0):
    print('Yes')
else:
    print('No')
