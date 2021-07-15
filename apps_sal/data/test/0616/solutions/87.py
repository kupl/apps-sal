N, M = list(map(int, input().split()))
K = []

for _ in range(M):
    a, _ = list(map(int, input().split()))
    k = 0
    for i in [int(a) - 1 for a in input().split()]:
        k |= (1 << i)
    K.append((a, k))

dp = [10**18] * (1 << N)
dp[0] = 0
for state in range(1 << N):
    for a, k in K:
        if dp[state | k] > dp[state] + a:
            dp[state | k] = dp[state] + a
ans = dp[(1 << N) - 1]
print((ans if ans < 10**18 else -1))

