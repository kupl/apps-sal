n, m = map(int, input().split())
key = []
for _ in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    bi = 0
    for i in c:
        bi += 2**(i - 1)
    key.append([a, bi])
dp = [10**10] * (2**n)
dp[0] = 0
for k in key:
    for b in range(2**n):
        dp[b | k[1]] = min(dp[b | k[1]], dp[b] + k[0])
if dp[-1] == 10**10:
    print(-1)
else:
    print(dp[-1])
