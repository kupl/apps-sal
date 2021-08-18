n, m = map(int, input().split())
a = [[i == '*' for i in input()] for j in range(n)]
t = ()
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if a[i][j] and a[i][j + 1] and a[i][j - 1] and a[i + 1][j] and a[i - 1][j]:
            if not t:
                t = (i, j)
            else:
                print('NO')
                return
if not t:
    print('NO')
    return
for i in range(t[0], -1, -1):
    if a[i][t[1]]:
        a[i][t[1]] = False
    else:
        break
for i in range(t[0] + 1, n):
    if a[i][t[1]]:
        a[i][t[1]] = False
    else:
        break
for i in range(t[1] - 1, -1, -1):
    if a[t[0]][i]:
        a[t[0]][i] = False
    else:
        break
for i in range(t[1] + 1, m):
    if a[t[0]][i]:
        a[t[0]][i] = False
    else:
        break
# print(a)
for el in a:
    for ell in el:
        if ell:
            print('NO')
            return
print('YES')
