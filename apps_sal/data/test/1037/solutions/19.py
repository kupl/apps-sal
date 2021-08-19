n = int(input())
a = sorted(((int(x), k) for (k, x) in enumerate(input().split())))
opt = [[0 for j in range(n + 1)] for i in range(n + 1)]
for i in reversed(list(range(n))):
    for j in range(i, n):
        (val, k) = a[j - i]
        opt[i][j] = max(val * abs(k - i) + opt[i + 1][j], val * abs(k - j) + opt[i][j - 1])
print(opt[0][n - 1])
