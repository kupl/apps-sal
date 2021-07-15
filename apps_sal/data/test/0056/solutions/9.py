read = lambda: list(map(int, input().split()))
n, t = read()
a = [[0] * 20 for i in range(20)]
b = [[0] * 20 for i in range(20)]
for k in range(t):
    for i in range(n):
        for j in range(n):
            b[i][j] = 0
    b[0][0] = 1
    for s in range(n):
        for i in range(s + 1):
            j = s - i
            a[i][j] += b[i][j]
            if a[i][j] > 1:
                r = a[i][j] - 1
                a[i][j] = 1
                b[i + 1][j] += r / 2
                b[i][j + 1] += r / 2
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += int(a[i][j] == 1)
print(cnt)

