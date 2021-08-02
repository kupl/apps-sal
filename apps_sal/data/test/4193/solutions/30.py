a = [list(map(int, input().split())) for i in range(3)]
n = int(input())

for k in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                a[i][j] = 0
    row0 = a[0] == [0, 0, 0]
    row1 = a[1] == [0, 0, 0]
    row2 = a[2] == [0, 0, 0]
    colum0 = [a[0][0], a[1][0], a[2][0]] == [0, 0, 0]
    colum1 = [a[0][1], a[1][1], a[2][1]] == [0, 0, 0]
    colum2 = [a[0][2], a[1][2], a[2][2]] == [0, 0, 0]
    diag0 = [a[0][0], a[1][1], a[2][2]] == [0, 0, 0]
    diag1 = [a[2][0], a[1][1], a[0][2]] == [0, 0, 0]
    if row0 or row1 or row2 or colum0 or colum1 or colum2 or diag0 or diag1:
        print('Yes')
        break
else:
    print('No')
