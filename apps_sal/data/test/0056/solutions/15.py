n, t = list(map(int, input().split()))
ans = 0
z = [[0 for i in range(n + 1)] for i in range(n + 1)]
e = [[0 for i in range(n + 1)] for i in range(n + 1)]
b = [[0 for i in range(n + 1)] for i in range(n + 1)]
for it in range(t):
    z[0][0] += 1
    if (ans >= n * (n + 1) // 2):
        break
    for i in range(n):
        for j in range(i + 1):
            if z[i][j] >= 1:
                if (b[i][j] == 0):
                    ans += 1
                b[i][j] = 1
                e[i][j] = z[i][j] - 1
                z[i][j] = 1
                z[i + 1][j] += e[i][j] / 2
                z[i + 1][j + 1] += e[i][j] / 2
                e[i][j] = 0
print(ans)
