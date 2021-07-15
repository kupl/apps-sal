INF = float("inf")

N, K, *H = map(int, open(0).read().split())
H = [0] + H

if N == K:
    print(0)
    return

dp = [0] + [INF] * N
for i in range(1, N - K + 1):
    dp = [INF] * i + [min(dp[k] + max(0, h - H[k]) for k in range(i - 1, j)) for j, h in enumerate(H[i:], i)]

print(min(dp))
