n = int(input())
a = []
for i in range(n):
    a.append(list(1 if c == '#' else 0 for c in input()))
for i in range(n):
    for j in range(n):
        if a[i][j]:
            if i + 2 >= n or j + 1 >= n or j == 0:
                print('NO')
                return
            if a[i + 1][j] + a[i + 2][j] + a[i + 1][j - 1] + a[i + 1][j + 1] != 4:
                print('NO')
                return
            a[i][j] = a[i + 1][j] = a[i + 2][j] = a[i + 1][j - 1] = a[i + 1][j + 1] = 0
print('YES')
