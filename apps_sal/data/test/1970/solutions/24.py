t = int(input())
while t:
    t += -1
    l = []
    mp = []
    for i in range(8):
        tmp = list(input())
        l.append(tmp)
        mp.append([0] * 8)
    i1, j1, i2, j2 = -1, -1, -1, -1
    for i in range(8):
        for j in range(8):
            if l[i][j] == 'K' and i1 == -1: i1, j1 = i, j
            if l[i][j] == 'K': i2, j2 = i, j
    if abs(i2 - i1) % 4 == 0 and abs(j2 - j1) % 4 == 0: print('YES')
    else: print('NO')
    if t != 0: input()
