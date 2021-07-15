n, m = list(map(int, input().split()))
u = []
u1 = []
for i in range(n):
    u.append(list(input()))
    u1.append(['.'] * m)
for i in range(n - 2):
    for j in range(m - 2):
        ok = True
        for k in range(3):
            if u[i][j + k] != '#' or u[i + k][j] != '#':
                ok = False
                break
##        print(ok)
        if ok:
            if u[i + 2][j + 1] != '#' or u[i + 2][j + 2] != '#' or u[i + 1][j + 2] != '#':
                ok = False
            else:
                for k in range(3):
                    u1[i][j + k] = '#'
                    u1[i + k][j] = '#'
                u1[i + 2][j + 1] = '#'  
                u1[i + 2][j + 2] = '#'
                u1[i + 1][j + 2] = '#'
ok = True
##for i in u:
##    print(i)
##for i in u1:
##    print(i)
for i in range(n):
    for j in range(m):
        if u[i][j] != u1[i][j]:
            ok = False
            break
    if not ok:
        break
if ok:
    print('YES')
else:
    print('NO')

