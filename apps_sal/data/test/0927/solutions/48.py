(N, M) = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
numk = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
dp = [0] + [-1] * (N + 1)
for i in range(N):
    for j in A:
        if i + numk[j] <= N:
            dp[i + numk[j]] = max(dp[i + numk[j]], dp[i] + 1)
m = N
ans = []
while m > 0:
    for i in A:
        if m - numk[i] >= 0 and dp[m - numk[i]] + 1 == dp[m]:
            ans.append(str(i))
            m -= numk[i]
            break
print(''.join(ans))
