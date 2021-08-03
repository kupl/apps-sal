n, m = map(int, input().split())
a = [input() for i in range(n)]
i = 0
while i < n and a[i] == '0' * (m + 2):
    i += 1
a = a[i:]
n = len(a)
dp = [[10 ** 5, 10 ** 5] for i in range(n)]
for i in range(n):
    l, r = a[i].find('1'), a[i].rfind('1')
    if l == r == -1:
        l, r = m + 1, 0
    if i == 0:
        dp[0] = [r, m + 1 - l]
    else:
        dp[i][0] = min(dp[i - 1][0] + 2 * r, dp[i - 1][1] + (m + 1)) + 1
        dp[i][1] = min(dp[i - 1][0] + m + 1, dp[i - 1][1] + 2 * (m + 1 - l)) + 1
ans = dp[-1][0] if dp else 0
print(ans)
