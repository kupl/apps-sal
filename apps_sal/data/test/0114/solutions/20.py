n, m = [int(x) for x in input().split()]
b = [[0] * m for i in range(n)]
a = []
arr = []
for i in range(n):
    c = [int(x) for x in input().split()]
    a.append(c)
for i in range(n - 1):
    for j in range(m - 1):
        if a[i][j] == a[i + 1][j] == a[i][j + 1] == a[i + 1][j + 1] == 1:
            b[i][j] = b[i + 1][j] = b[i][j + 1] = b[i + 1][j + 1] = 1
            arr.append((i + 1, j + 1))
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print(-1)
            return
print(len(arr))
for item in arr:
    print(*item)
