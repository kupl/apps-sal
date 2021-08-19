[n, k] = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
b.insert(0, 0)
a.insert(0, 0)
s = sum(b) * k
f = [[0 for i in range(0, 4 * s + 1)] for j in range(0, n + 1)]
for i in range(0, n + 1):
    a[i] = a[i] - k * b[i]
for i in range(1, n + 1):
    for j in range(s, 3 * s + 1):
        f[i][j] = f[i - 1][j]
        if j - a[i] == 2 * s or f[i - 1][j - a[i]] > 0:
            f[i][j] = max(f[i][j], f[i - 1][j - a[i]] + b[i])
if f[n][2 * s]:
    print(f[n][2 * s] * k)
else:
    print(-1)
