N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)
f = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [-float('inf')] * (N + 1)
dp[0] = 0
for i in range(N + 1):
    nxt = dp[i]
    for aj in A:
        if i - f[aj] < 0:
            continue
        nxt = max(nxt,
                  dp[i - f[aj]] + 1)
    dp[i] = nxt
keta = dp[N]
ans = ""
matchs = N
while keta > 0:
    for aj in A:
        if matchs - f[aj] < 0:
            continue
        if dp[matchs - f[aj]] == keta - 1:
            ans += str(aj)
            matchs -= f[aj]
            keta -= 1
            break
print(ans)
