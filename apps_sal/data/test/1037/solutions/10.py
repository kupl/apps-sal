N = int(input())
A = [(a, i) for i, a in enumerate(map(int, input().split()), start=1)]
A.sort(reverse=True)

dp = [[0] * (N + 1) for _ in range(N + 1)]

for s, (a, i) in enumerate(A):
    for l in range(s + 1):
        r = s - l
        L = dp[l][r] + a * (i - (l + 1))
        R = dp[l][r] + a * (N - r - i)

        if dp[l + 1][r] < L:
            dp[l + 1][r] = L
        if dp[l][r + 1] < R:
            dp[l][r + 1] = R

ans = 0
for i in range(N + 1):
    ans = max(ans, dp[i][N - i])
print(ans)
