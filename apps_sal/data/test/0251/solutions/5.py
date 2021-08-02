from sys import stdin
n, m = list(map(int, stdin.readline().strip().split()))
s = tuple(map(int, stdin.readline().strip().split()))
ma = max(s)
mi = min(s)
dp = [0 for i in range(ma + 3)]
for i in s:
    dp[i] += 1
for i in range(len(dp) - 2, -1, -1):
    dp[i] += dp[i + 1]
x = 0
ans = 0
acum = 0
l = -1
for i in range(len(dp) - 2, mi - 1, -1):
    dp[i] += dp[i + 1]
    if dp[i] - acum > m:
        acum = dp[i + 1]
        ans += 1
        l = i
if l != mi and mi != ma:
    ans += 1
print(ans)
