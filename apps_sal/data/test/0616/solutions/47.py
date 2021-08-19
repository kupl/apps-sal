n, m = map(int, input().split())
key = []
for _ in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    bi = 0
    for i in c:
        bi += 1 << (i - 1)
    key.append([a, bi])
# print(key)

INF = 2**24
dp = [INF] * (1 << n)
dp[0] = 0
for k in key:
    for b in range(1 << n):
        dp[b | k[1]] = min(dp[b | k[1]], dp[b] + k[0])
        # print(b,k[1],b|k[1],dp)

print(-1 if dp[-1] == INF else dp[-1])
