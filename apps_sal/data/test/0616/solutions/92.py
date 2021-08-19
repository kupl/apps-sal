(N, M) = map(int, input().split())
dp = [float('inf')] * 2 ** N
dp[0] = 0
for i in range(1, M + 1):
    (a, b) = map(int, input().split())
    c = list(map(int, input().split()))
    d = 0
    for j in range(1, N + 1):
        if j in c:
            d += 2 ** (j - 1)
    for j in range(2 ** N):
        dp[j | d] = min(dp[j | d], dp[j] + a)
print(dp[-1] if dp[-1] != float('inf') else -1)
