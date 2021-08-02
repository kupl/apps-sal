n = int(input())
s1 = input() + ' '
s2 = input() + ' '
mod = 10**9 + 7

s = []
for i in range(n):
    if s1[i] == s2[i]:
        s.append(1)
        continue
    if s1[i] == s1[i + 1]:
        continue
    s.append(2)

dp = [0] * len(s)
dp[0] = 3 if s[0] == 1 else 6
for i in range(len(s) - 1):
    if s[i] == 1 and s[i + 1] == 1:
        dp[i + 1] = dp[i] * 2
    if s[i] == 1 and s[i + 1] == 2:
        dp[i + 1] = dp[i] * 2
    if s[i] == 2 and s[i + 1] == 1:
        dp[i + 1] = dp[i]
    if s[i] == 2 and s[i + 1] == 2:
        dp[i + 1] = dp[i] * 3
    dp[i + 1] %= mod
print((dp[-1]))
