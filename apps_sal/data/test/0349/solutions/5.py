(n, m) = list(map(int, input().split()))
a = [None] * n
b = [None] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
for i in range(n):
    b[i] = [int(x) for x in input().split()]
mi = [[None] * m for _ in range(n)]
ma = [[None] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        mi[i][j] = min(a[i][j], b[i][j])
        ma[i][j] = max(a[i][j], b[i][j])
for i in range(n):
    for j in range(m):
        if i > 0 and mi[i][j] <= mi[i - 1][j] or (i < n - 1 and mi[i][j] >= mi[i + 1][j]) or (j > 0 and mi[i][j] <= mi[i][j - 1]) or (j < m - 1 and mi[i][j] >= mi[i][j + 1]):
            print('Impossible')
            raise SystemExit(0)
        if i > 0 and ma[i][j] <= ma[i - 1][j] or (i < n - 1 and ma[i][j] >= ma[i + 1][j]) or (j > 0 and ma[i][j] <= ma[i][j - 1]) or (j < m - 1 and ma[i][j] >= ma[i][j + 1]):
            print('Impossible')
            raise SystemExit(0)
print('Possible')
