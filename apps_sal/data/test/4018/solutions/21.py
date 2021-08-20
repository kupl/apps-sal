import math
(n, k) = map(int, input().split())
dp = [[0] * 102 for i in range(102)]
s = input()
last = [-1] * 26
for i in range(0, 101):
    dp[i][0] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ch = s[i - 1]
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        sub = last[ord(ch) - ord('a')]
        if sub == -1:
            continue
        sub -= 1
        dp[i][j] -= dp[sub][j - 1]
    last[ord(ch) - ord('a')] = i
ans = int(0)
for i in range(n, -1, -1):
    if dp[n][i] >= k:
        ans += k * (n - i)
        k = 0
    elif k > 0:
        k -= dp[n][i]
        ans += (n - i) * dp[n][i]
    else:
        break
if k > 0:
    ans = -1
print(ans)
