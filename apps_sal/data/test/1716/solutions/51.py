n, m, q = map(int, input().split())
a = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    l, r = map(int, input().split())
    a[l - 1][r - 1] += 1

for i in range(n):
    for j in range(1, n):
        a[i][j] += a[i][j - 1]

for j in range(n):
    for i in range(1, n):
        a[i][j] += a[i - 1][j]

for i in range(q):
    l, r = map(int, input().split())
    ans = a[r - 1][r - 1]
    if l > 1:
        ans += a[l - 2][l - 2] - a[r - 1][l - 2] - a[l - 2][r - 1]
    print(ans)
