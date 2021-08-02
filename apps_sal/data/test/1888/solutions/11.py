n, m = map(int, input().split())
f = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    f[a - 1][b - 1] = c
for i in range(n):
    for j in range(n):
        if f[i][j] > 0:
            for k in range(n):
                if f[j][k] > 0:
                    buf = min(f[i][j], f[j][k])
                    f[i][j] -= buf
                    f[j][k] -= buf
                    f[i][k] += buf
for i in range(n):
    f[i][i] = 0
print(sum(map(sum, f)))
