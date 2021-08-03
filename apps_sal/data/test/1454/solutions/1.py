n, m = list(map(int, input().split()))
k = 0
a = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split()))

b = [0] * n
c = [0] * n
for i in range(n):
    b[i] = [0] * m
    c[i] = [0] * m
    for j in range(m):
        b[i][j] = [0, 0]
        c[i][j] = [0, 0]

for i in range(n):
    for j in range(m - 1):
        if a[i][j] >= a[i][j + 1] and a[i][j + 1] != 0:
            k = 1
for j in range(m):
    for i in range(n - 1):
        if a[i][j] >= a[i + 1][j] and a[i + 1][j] != 0:
            k = 1

for i in range(n - 1, 0, -1):
    for j in range(m - 1, 0, -1):
        if a[i][j] == 0:
            a[i][j] = min(a[i + 1][j] - 1, a[i][j + 1] - 1)

for i in range(n):
    for j in range(m - 1):
        if a[i][j] >= a[i][j + 1] and a[i][j + 1] != 0:
            k = 1
for j in range(m):
    for i in range(n - 1):
        if a[i][j] >= a[i + 1][j] and a[i + 1][j] != 0:
            k = 1

ans = 0
for i in range(n):
    ans += sum(a[i])
if k == 1:
    print(-1)
else:
    print(ans)
