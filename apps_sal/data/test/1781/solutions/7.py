n, k = (int(i) for i in input().split())
z = [[i for i in input()] for i in range(n)]
a1 = []
a2 = []
a3 = []
r = 0
for i in range(n):
    for j in range(12):
        t = 0
        t = (j != 0 and z[i][j-1] == 'S') + (j != 11 and z[i][j+1] == 'S')
        if z[i][j] == 'P' or z[i][j] == 'S':
            r += t
        elif z[i][j] == '.':
            if t == 0:
                a1.append((i, j))
            elif t == 1:
                a2.append((i, j))
            else:
                a3.append((i, j))
for i in a1:
    if k != 0:
        z[i[0]][i[1]] = 'x'
        k -= 1
    else:
        break
for i in a2:
    if k != 0:
        z[i[0]][i[1]] = 'x'
        k -= 1
        r += 1
    else:
        break
for i in a3:
    if k != 0:
        z[i[0]][i[1]] = 'x'
        k -= 1
        r += 2
    else:
        break
print(r)
for i in z:
    print(*i, sep='')
