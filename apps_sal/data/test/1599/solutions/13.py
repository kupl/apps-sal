string = input()
# dp represents a list of the counts to each point in the string
n = int(input())
a, b = [0 for i in range(n)], [0 for i in range(n)]
for i in range(n):
    a[i], b[i] = list(map(int, input().split()))
dp = [0] * (len(string))
for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        dp[i + 1] = dp[i] + 1
    else:
        dp[i + 1] = dp[i]
dp.append(dp[-1])

for i in range(n):
    print(dp[b[i] - 1] - dp[a[i] - 1])
