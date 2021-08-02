# fdf_2791
n = int(input())
a = [list(input()) for i in range(n)]
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if a[i][j] == a[i - 1][j] == a[i][j + 1] == a[i + 1][j] == a[i][j - 1] == '#':
            a[i][j] = a[i - 1][j] = a[i][j + 1] = a[i + 1][j] = a[i][j - 1] = '.'

print((sum(a[i].count('#')for i in range(n))) == 0 and "YES" or "NO")
