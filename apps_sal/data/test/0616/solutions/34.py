N, M = map(int, input().split())
key = []
for i in range(M):
    a, b = map(int, input().split())
    C = list(map(int, input().split()))
    s = 0
    for i in range(b):
        C[i] -= 1
        s = s | 1 << C[i]
    key.append((s, a))
INF = float("inf")
dp = [INF for _ in range(1 << N)]
dp[0] = 0
for s in range(1 << N):
    for i in range(M):
        t = s | key[i][0]
        dp[t] = min(dp[t], dp[s] + key[i][1])
if dp[-1] == INF:
    ans = -1
else:
    ans = dp[-1]
print(ans)
