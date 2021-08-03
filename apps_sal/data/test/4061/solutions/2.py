from sys import stdin
s = stdin.readline().strip()
s1 = stdin.readline().strip()
dp = [-1 for i in range(len(s1) + 1)]
dp1 = [-1 for i in range(len(s1) + 1)]
x = 0
for i in range(len(s)):
    if s[i] == s1[x]:
        dp[x + 1] = i
        x += 1
        if x >= len(s1):
            break
x = len(s1) - 1
y = 1
dp[0] = -1
dp1[0] = len(s)
for i in range(len(s) - 1, -1, -1):
    if s[i] == s1[x]:
        dp1[y] = i
        x -= 1
        y += 1
        if x < 0:
            break

ans = 0
for i in range(len(s1) + 1):
    ans = max(dp1[len(s1) - i] - dp[i] - 1, ans)
    ans = max(dp[len(s1) - i] - dp1[i] - 1, ans)


print(ans)
