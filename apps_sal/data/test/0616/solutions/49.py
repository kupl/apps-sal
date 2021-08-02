N, M = map(int, input().split())
dp = [10**10] * (1 << N)
dp[0] = 0
for i in range(M):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    d = 0
    for j in c:
        d |= 1 << j - 1
    for k in range(1 << N):
        dp[k | d] = min(dp[k | d], dp[k] + a)
if dp[-1] == 10**10:
    print(-1)
else:
    print(dp[-1])
