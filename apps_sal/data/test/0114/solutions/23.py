n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

b = [[0] * m for _ in range(n)]

op = []

for i in range(n - 1):
    for j in range(m - 1):
        if a[i][j] == a[i + 1][j] == a[i][j + 1] == a[i + 1][j + 1] == 1:
            op.append((i, j))
            b[i][j] = b[i + 1][j] = b[i][j + 1] = b[i + 1][j + 1] = 1

ok = True

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            ok = False

if not ok:
    print(-1)
else:
    print(len(op))
    for x in op:
        print(x[0] + 1, x[1] + 1)
