n, x = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
dp = [[-10**18 for i in range(5)] for j in range(len(A))]

for i in range(n - 1, -1, -1):
    if 1:
        nxt = [0, 0, 0, 0, 0]
        if i != n - 1:
            nxt = dp[i + 1]
        coeff = [0, 1, x, 1, 0]
        for j in range(5):
            for xx in range(j, len(coeff)):
                dp[i][j] = max(dp[i][j], coeff[xx] * A[i] + nxt[xx])


print(max(dp[0]))
