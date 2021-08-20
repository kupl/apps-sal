n = int(input())
c = [0 for _ in range(n - 1)]
s = [0 for _ in range(n - 1)]
f = [0 for _ in range(n - 1)]
for i in range(n - 1):
    (c[i], s[i], f[i]) = list(map(int, input().split()))
t = [[-1 for _ in range(n)] for _ in range(n - 1)]
for i in range(n - 1):
    t[i][i] = s[i]
for i in range(n - 1):
    for j in range(i, n):
        if i != j:
            t[i][j] = t[i][j - 1] + c[j - 1]
            if j == n - 1:
                break
            if t[i][j] - t[j][j] <= 0:
                t[i][j] = t[j][j]
            elif (t[i][j] - t[j][j]) % f[j] != 0:
                t[i][j] = t[j][j] + ((t[i][j] - t[j][j]) // f[j] + 1) * f[j]
for i in range(n - 1):
    print(t[i][n - 1])
print(0)
