n, m = map(int, input().split())
a = []
for i in range(n):
    s = input()
    a.append(s)
for i in range(n):
    for j in range(m):
        if a[i][j] == '.':
            continue
        if i >= 2 and j >= 2:
            if a[i - 2][j - 2] == '#' and a[i - 2][j - 1] == '#' and a[i - 2][j] == '#' \
                    and a[i - 1][j] == '#' and a[i - 1][j - 2] == '#' and a[i][j - 1] == '#' and a[i][j - 2] == '#':
                continue
        if i >= 1 and i <= n - 2 and j >= 2 and a[i - 1][j - 2] == '#' and a[i - 1][j - 1] == '#' and a[i - 1][j] == '#' \
                and a[i][j - 2] == '#' and a[i + 1][j - 2] == '#' and a[i + 1][j - 1] == '#' and a[i + 1][j] == '#':
            continue
        if i <= n - 3 and j >= 2 and a[i][j - 1] == '#' and a[i][j - 2] == '#' and a[i + 1][j] == '#' \
                and a[i + 1][j - 2] == '#' and a[i + 2][j] == '#' and a[i + 2][j - 1] == '#' and a[i + 2][j - 2] == '#':
            continue
        if i <= n - 3 and j >= 1 and j <= m - 2 and a[i][j - 1] == '#' and a[i][j + 1] == '#' and a[i + 1][j - 1] == '#' \
                and a[i + 1][j + 1] == '#' and a[i + 2][j] == '#' and a[i + 2][j - 1] == '#' and a[i + 2][j + 1] == '#':
            continue
        if i <= n - 3 and j <= m - 3 and a[i][j + 1] == '#' and a[i][j + 2] == '#' and a[i + 1][j] == '#' \
                and a[i + 1][j + 2] == '#' and a[i + 2][j] == '#' and a[i + 2][j + 1] == '#' and a[i + 2][j + 2] == '#':
            continue
        if i <= n - 2 and i >= 1 and j <= m - 3 and a[i - 1][j] == '#' and a[i - 1][j + 1] == '#' and a[i - 1][j + 2] == '#' \
                and a[i][j + 2] == '#' and a[i + 1][j] == '#' and a[i + 1][j + 1] == '#' and a[i + 1][j + 2] == '#':
            continue
        if i >= 2 and j <= m - 3 and a[i - 2][j] == '#' and a[i - 2][j + 1] == '#' and a[i - 2][j + 2] == '#' \
                and a[i - 1][j] == '#' and a[i - 1][j + 2] == '#' and a[i][j + 1] == '#' and a[i][j + 2] == '#':
            continue
        if i >= 2 and j <= m - 2 and j >= 1 and a[i - 2][j - 1] == '#' and a[i - 2][j] == '#' and a[i - 2][j + 1] == '#' \
                and a[i - 1][j - 1] == '#' and a[i - 1][j + 1] == '#' and a[i][j - 1] == '#' and a[i][j + 1] == '#':
            continue
        print('NO')
        return
print('YES')
