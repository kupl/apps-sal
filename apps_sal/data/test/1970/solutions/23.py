t = int(input())
for _ in range(t):
    if _ != 0:
        tmp = input()
    pos = []
    n = 8
    g = []
    for i in range(n):
        g.append([i for i in input()])
    for i in range(n):
        for j in range(n):
            if g[i][j] == 'K':
                pos.append((i, j))
    ok = False
    for i in range(n):
        for j in range(n):
            if i % 2 == pos[0][0] % 2 and i % 2 == pos[1][0] % 2 and (j % 2 == pos[0][1] % 2) and (j % 2 == pos[1][1] % 2):
                dist1 = (i - pos[0][0], j - pos[0][1])
                dist2 = (i - pos[1][0], j - pos[1][1])
                if dist1[0] - dist2[0] % 4 == 0 and dist1[1] - dist2[1] % 4 == 0:
                    ok = True
    print('YES' if ok else 'NO')
