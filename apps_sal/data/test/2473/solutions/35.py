n, K = map(int, input().split())
xy = []
x = []
y = []
for _ in range(n):
    X, Y = map(int, input().split())
    x.append(X + 10**9)
    y.append(Y + 10**9)
    xy.append((X + 10**9, Y + 10**9))
x.sort()
y.sort()
xy.sort()
num = [[0] * (n + 1)for _ in range(n + 1)]
for xx in xy:
    for i in range(n):
        if x[i] == xx[0]:
            break
    for j in range(n):
        if y[j] == xx[1]:
            break
    num[i + 1][j + 1] += 1
for i in range(n):
    for j in range(n):
        num[i + 1][j + 1] += num[i + 1][j]
for i in range(n):
    for j in range(n):
        num[i + 1][j + 1] += num[i][j + 1]
ans = 10**20
for i in range(n):
    for j in range(n):
        for k in range(i + 1, n + 1):
            for l in range(j + 1, n + 1):
                if num[k][l] - num[i][l] - num[k][j] + num[i][j] >= K:
                    r = (y[l - 1] - y[j]) * (x[k - 1] - x[i])
                    ans = min(ans, r)
print(ans)
