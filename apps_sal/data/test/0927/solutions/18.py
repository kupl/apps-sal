N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)
INF = float('inf')
dp = [-INF]*(N + 5)
needs = [2, 5, 5, 4, 5, 6, 3, 7, 6]
can_use = {k: needs[k-1] for k in A}
dp[0] = 0
for i in range(2, N+1):
    for v in list(can_use.values()):
        if i - v < 0:
            continue
        dp[i] = max(dp[i], dp[i-v]+1)
ans = ''
i = N
while i != 0:
    for k, v in list(can_use.items()):
        if i - v < 0:
            continue
        while dp[i] == dp[i-v] + 1:
            ans += str(k)
            i -= v
print(ans)

