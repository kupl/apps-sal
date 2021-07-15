n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
# print(a)
dp = [[0 for i in range(k + 1)] for i in range(n + 1)]
i, j = 1, 2
prev_max = [0 for i in range(k + 1)]
ans = 0
while i < n + 1:
    while j < n + 1 and a[j - 1] - a[i - 1] <= 5:
        j += 1
    for c in range(k):
        dp[j - 1][c + 1] = max(dp[j - 1][c + 1], prev_max[c] + (j - i))
        ans = max(ans, dp[j - 1][c + 1])
    for c in range(k):
        prev_max[c] = max(prev_max[c], dp[i][c])
    # print(i, j)
    # print(prev_max)
    i = i + 1
# print(dp)
print(ans)

