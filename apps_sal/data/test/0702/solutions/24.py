n = int(input())
a = []
fin = []
for i in range(n):
    b = input()
    v = [0] * len(b)
    a.append(b)
    fin.append(v)

for i in range(n):
    for j in range(n):
        if(a[i][j] == '#'):
            fin[i][j] = 1

for i in range(1, n - 1):
    for j in range(1, len(a[i]) - 1):
        if(a[i][j] == '.' and a[i - 1][j] == '.' and a[i][j + 1] == '.' and a[i][j - 1] == '.' and a[i + 1][j] == '.' and fin[i][j] == 0 and fin[i - 1][j] == 0 and fin[i][j + 1] == 0 and fin[i][j - 1] == 0 and fin[i + 1][j] == 0):
            fin[i][j] = fin[i - 1][j] = fin[i][j + 1] = fin[i][j - 1] = fin[i + 1][j] = 1
poss = 0
for i in range(n):
    for j in range(n):
        if(fin[i][j] == 0):
            poss = 1
            break
if(poss):
    print('NO')
else:
    print('YES')
