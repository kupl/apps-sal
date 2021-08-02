n, m = [int(i) for i in input().split()]
a = [[0] * 4 for i in range(n)]
for i in range(m):
    if i < 2 * n:
        if i % 2 == 0:
            a[i // 2][0] = i + 1
        else:
            a[i // 2][1] = i + 1
    else:
        if i % 2 == 0:
            a[(i - 2 * n) // 2][2] = i + 1
        else:
            a[(i - 2 * n) // 2][3] = i + 1
j = 0
while j < m:
    for i in range(n):
        if a[i][2] > 0:
            print(a[i][2], end=' ')
            j += 1
        if a[i][0] > 0:
            print(a[i][0], end=' ')
            j += 1
        if a[i][3] > 0:
            print(a[i][3], end=' ')
            j += 1
        if a[i][1] > 0:
            print(a[i][1], end=' ')
            j += 1
