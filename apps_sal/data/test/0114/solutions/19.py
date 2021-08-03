n, m = map(int, input().split())
ans = []
b = [[0] * m for i in range(n)]
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n - 1):
    for j in range(m - 1):
        if a[i][j] == 1 and a[i + 1][j] == 1 and a[i][j + 1] == 1 and a[i + 1][j + 1] == 1:
            b[i][j] = 1
            b[i + 1][j] = 1
            b[i][j + 1] = 1
            b[i + 1][j + 1] = 1
            ans.append([i + 1, j + 1])
if b != a:
    print(-1)
else:
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])
