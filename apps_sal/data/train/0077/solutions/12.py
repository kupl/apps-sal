from sys import stdin

test = stdin.readlines()
inf = float('infinity')

q = int(test[0])
k = 1
for _ in range(q):
    n = int(test[k])

    h, c = [], []
    for j in range(k + 1, k + n + 1):
        x, y = list(map(int, test[j].split()))
        h.append(x)
        c.append(y)

    dp = [[0, c[0], 2 * c[0]]]
    dp += [[0, 0, 0] for i in range(n - 1)]

    for i in range(1, n):
        for j in range(3):
            x = (dp[i - 1][0] if h[i - 1] != h[i] + j else inf)
            y = (dp[i - 1][1] if h[i - 1] + 1 != h[i] + j else inf)
            z = (dp[i - 1][2] if h[i - 1] + 2 != h[i] + j else inf)
            dp[i][j] = min(x, y, z) + j * c[i]

    print(min(dp[n - 1]))

    k += n + 1
