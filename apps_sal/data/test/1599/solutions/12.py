s = input()
n = int(input())
a, b = [0 for i in range(n)], [0 for i in range(n)]
for i in range(0, n):
    a[i], b[i] = list(map(int, input().split()))
# dp represents a list of the counts to each point in the string
dp = [0] * (len(s))
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        dp[i + 1] = dp[i] + 1
    else:
        dp[i + 1] = dp[i]

for i in range(0, n):
    print(dp[b[i] - 1] - dp[a[i] - 1])
