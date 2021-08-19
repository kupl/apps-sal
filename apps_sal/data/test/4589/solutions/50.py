X, Y = map(int, input().split())
F = list(list(input()) for _ in range(X))
DX = [-1, -1, -1, 0, 0, 1, 1, 1]
DY = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(X):
    for j in range(Y):
        if F[i][j] == '.':
            cnt = 0
            for k in range(8):
                x = i + DX[k]
                y = j + DY[k]
                if 0 <= x < X and 0 <= y < Y and F[x][y] == '#':
                    cnt += 1
            F[i][j] = str(cnt)

for f in F:
    print(''.join(f))
