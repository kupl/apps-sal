import sys
input = sys.stdin.readline
n = int(input())
s = input()
a = list(map(int, input().split()))
dp = [0] * 4
for i in range(n):
    if s[i] == 'h':
        dp[0] += a[i]
    elif s[i] == 'a':
        dp[1] = min(dp[0], a[i] + dp[1])
    elif s[i] == 'r':
        dp[2] = min(dp[1], a[i] + dp[2])
    elif s[i] == 'd':
        dp[3] = min(dp[2], a[i] + dp[3])
print(min(dp))
