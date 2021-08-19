(n, m) = map(int, input().split())
a = list(map(int, input().split()))
dp = [-1] * (n * 18)
for i in range(n * 9):
    dp[i] = 0
lis = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for i in range(n):
    cnt = -float('inf')
    for j in a:
        cnt = max(cnt, dp[i + 1 - lis[j]] * 10 + j)
    dp[i + 1] = cnt
print(dp[n])
