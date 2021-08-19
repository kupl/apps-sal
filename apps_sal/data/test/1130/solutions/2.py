def R():
    return map(int, input().split())


(n, m, k) = R()
cls = [list((i for (i, x) in enumerate(map(int, input())) if x)) for _ in range(n)]
dp = [[n * m] * (k + 1) for i in range(n + 1)]
dp.append([0] * (k + 1))
for i in range(n):
    row = cls[i]
    c2l = [m + 1] * (m + 1)
    c2l[0] = row[-1] - row[0] + 1 if row else 0
    c2l[len(row)] = 0
    for r in range(len(row)):
        for l in range(r + 1):
            c2l[len(row) - (r - l + 1)] = min(c2l[len(row) - (r - l + 1)], row[r] - row[l] + 1)
    for j in range(k + 1):
        for (c, l) in enumerate(c2l):
            if j + c <= k and l < m + 1:
                dp[i][j] = min(dp[i][j], dp[i - 1][j + c] + l)
print(min(dp[n - 1]))
