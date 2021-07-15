n = int(input())
a = []
for i in range(n):
    a.append(list(input()))

for i in range(n):
    for j in range(n):
        if a[i][j] == '.':
            if n - i < 3 or j == 0 or j == n - 1 or a[i + 1][j] == '#'\
                    or a[i + 2][j] == '#' or a[i + 1][j + 1] == '#' or a[i + 1][j - 1] == '#' or a[i][j] == '#':
                print('NO')
                return

            a[i][j] = '#'
            a[i + 1][j] = '#'
            a[i + 2][j] = '#'
            a[i + 1][j - 1] = '#'
            a[i + 1][j + 1] = '#'
print('YES')

