n = int(input())
mat = []
for i in range(n):
    mat.append(list(input()))
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if mat[i][j] == '.':
            if mat[i + 1][j] == '.' and mat[i - 1][j] == '.' and (mat[i][j - 1] == '.') and (mat[i][j + 1] == '.'):
                mat[i + 1][j] = '#'
                mat[i - 1][j] = '#'
                mat[i][j - 1] = '#'
                mat[i][j + 1] = '#'
                mat[i][j] = '#'
cnt = 0
for i in range(n):
    for j in range(n):
        if mat[i][j] == '#':
            cnt += 1
print('YES' if cnt == n * n else 'NO')
