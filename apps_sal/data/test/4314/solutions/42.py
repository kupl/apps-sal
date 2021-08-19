N, M = map(int, input().split())
ls = []
for i in range(N):
    ls.append(list(input()))
yoko = []
tate = [i for i in range(M)]
for i in range(N):
    if ls[i].count('.') == M:
        yoko.append(i)
for i in range(N):
    for j in range(M):
        if ls[i][j] == '#' and j in tate:
            tate.remove(j)
tate2 = list(range(M))
for i in range(M):
    if i in tate:
        tate2.remove(i)

ansls = []
for i in range(N):
    if not i in yoko:
        ansls.append([ls[i][j] for j in tate2])
for i in ansls:
    print(''.join(i))
