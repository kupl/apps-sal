n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
L = [2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-float('inf')] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in range(m):
        if i - L[A[j] - 1] < 0:
            None
        else:
            dp[i] = max(dp[i - L[A[j] - 1]] + 1, dp[i])
A.sort()
A.reverse()
cur = n
ans = ''
while cur != 0:
    for i in range(m):
        temp = A[i]
        if cur - L[temp - 1] >= 0:
            if dp[cur - L[temp - 1]] == dp[cur] - 1:
                ans = ans + str(temp)
                cur -= L[temp - 1]
                break
print(ans)
