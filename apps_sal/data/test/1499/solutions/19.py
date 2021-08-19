(n, m) = map(int, input().split())
a = [[0] * 4 for i in range(n)]
for i in range(n):
    if i * 2 + 1 <= m:
        a[i][0] = i * 2 + 1
    if i * 2 + 1 + 2 * n <= m:
        a[i][1] = i * 2 + 1 + 2 * n
    if i * 2 + 2 + n * 2 <= m:
        a[i][2] = i * 2 + 2 + 2 * n
    if i * 2 + 2 <= m:
        a[i][3] = i * 2 + 2
for i in range(n):
    if a[i][1]:
        print(a[i][1], end=' ')
    if a[i][0]:
        print(a[i][0], end=' ')
    if a[i][2]:
        print(a[i][2], end=' ')
    if a[i][3]:
        print(a[i][3], end=' ')
