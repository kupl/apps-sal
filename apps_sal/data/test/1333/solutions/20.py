n, m = list(map(int, input().split()))
a = [['.' for col in range(m)] for row in range(n)]
cur = 'L'
for i in range(0, n, 2):
    if cur == 'L':
        for j in range(m):
            a[i][j] = '#'
        cur = 'R'
        if i < n - 1:
            a[i + 1][m - 1] = '#'
    elif cur == 'R':
        for j in range(m - 1, -1, -1):
            a[i][j] = '#'
        cur = 'L'
        if i < n - 1:
            a[i + 1][0] = '#'
for row in a:
    print(''.join(row))
