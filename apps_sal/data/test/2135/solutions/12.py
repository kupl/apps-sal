n, m = list(map(int, input().split()))
a = [' ' + input() for i in range(n)]
a = [' '*(m+1)] + a
q = int(input())

col = [[0 for i in range(m+1)] for i in range(n+1)]
row = [[0 for i in range(m+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        col[i][j] = col[i-1][j] + col[i][j-1] - col[i-1][j-1] + (a[i][j] == '.' and a[i-1][j] == '.')
        row[i][j] = row[i-1][j] + row[i][j-1] - row[i-1][j-1] + (a[i][j] == '.' and a[i][j-1] == '.')

for i in range(q):
    r1, c1, r2, c2 = list(map(int, input().split()))
    print((col[r2][c2] - col[r1][c2] - col[r2][c1-1] + col[r1][c1-1] \
        + row[r2][c2] - row[r2][c1] - row[r1-1][c2] + row[r1-1][c1]))

