N = int(input())
for i in range(N):
    if i > 0:
        input()
    Pos = []
    for i in range(8):
        S = input().strip()
        for j in range(8):
            if S[j] == 'K':
                Pos.append((i, j))
    (Dx, Dy) = (abs(Pos[0][0] - Pos[1][0]), abs(Pos[0][1] - Pos[1][1]))
    if (Dx == 0 or Dx == 4) and (Dy == 0 or Dy == 4):
        print('YES')
    else:
        print('NO')
