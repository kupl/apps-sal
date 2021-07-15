n = int(input())
a = [list(input()) for i in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] == '#':
            if (i < n - 2 and j >= 1 and j <= n - 2 and a[i + 1][j - 1] == '#' and a[i + 1][j] == '#' and a[i + 1][j + 1] == '#' and a[i + 2][j] == '#'):
                a[i][j] = '.'
                a[i + 1][j - 1] = '.'
                a[i + 1][j] = '.'
                a[i + 1][j + 1] = '.'
                a[i + 2][j] = '.'
            else:
                print('NO')
                return
print('YES')
