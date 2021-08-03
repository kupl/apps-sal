n = int(input())
if n == 1:
    print(int(input()))
    print(0)
    return
arr = [list(map(int, input().split(' '))) for _ in range(n)]
a = [[0] * n for _ in range(n)]
b = [[0] * n for _ in range(n)]
for i in range(n):
    a[i][i] = arr[i][i]
for i in range(n):
    for j in range(i + 1, n):
        a[i][j] = (arr[i][j] + arr[j][i]) / 2
        a[j][i] = (arr[i][j] + arr[j][i]) / 2
        b[i][j] = (arr[i][j] - arr[j][i]) / 2
        b[j][i] = -(arr[i][j] - arr[j][i]) / 2
for i in a:
    print(*i)
for i in b:
    print(*i)
