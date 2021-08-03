n = int(input())
b = list(map(int, input().split()))
dp = [[1] * n for i in range(n)]
d, k = {}, 0
for i in range(n):
    if b[i] not in d:
        d[b[i]] = k
        k += 1
    b[i] = d[b[i]]
d.clear()
for i in range(n):
    for j in range(i):
        dp[i][b[j]] = max(1 + dp[j][b[i]], dp[i][b[j]])
ans = 0
for l in dp:
    ans = max(ans, max(l))
print(ans)
