N, Ma, Mb = list(map(int, input().split()))

sum_a = 0
sum_b = 0
A = []
B = []
C = []
for _ in range(N):
    a, b, c = list(map(int, input().split()))
    sum_a += a
    sum_b += b
    A.append(a)
    B.append(b)
    C.append(c)

inf = 10 ** 9 + 7
# 3次元dpを考える
dp = [[[inf] * (sum_b + 1) for _ in range(sum_a + 1)] for _ in range(N + 1)]

dp[0][0][0] = 0
for i in range(N):
    for sa in range(sum_a):
        for sb in range(sum_b):
            if sa - A[i] >= 0 and sb - B[i] >= 0:
                dp[i + 1][sa][sb] = min(dp[i][sa - A[i]]
                                        [sb - B[i]] + C[i], dp[i][sa][sb])
            else:
                dp[i + 1][sa][sb] = min(dp[i][sa][sb], dp[i + 1][sa][sb])

ans = inf
for i in range(1, sum_a + 1):
    for j in range(1, sum_b + 1):
        if Ma * j == Mb * i:
            ans = min(ans, dp[N][i][j])

print((ans if ans != inf else -1))
