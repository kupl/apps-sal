n, m, q = map(int, input().split())
a = [[0 for _ in range(n + 1)]for _ in range(n + 1)]
for _ in range(m):
    l, r = map(int, input().split())
    a[l][r] += 1
for i in range(n + 1):
    for j in range(n):
        a[i][j + 1] += a[i][j]
for i in range(n):
    for j in range(n + 1):
        a[i + 1][j] += a[i][j]
for _ in range(q):
    l, r = map(int, input().split())
    print(a[r][r] - a[r][l - 1] - a[l - 1][r] + a[l - 1][l - 1])
