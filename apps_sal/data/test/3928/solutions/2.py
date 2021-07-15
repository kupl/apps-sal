import collections

# The first line contains three positive integers, separated by spaces:
# n, a and b (1≤n,a,b≤5000) — the length of the string, the cost to compress a one-character string
# and the cost to compress a string that appeared before.

n, a, b = list(map(int, input().split()))

# The second line contains a single string s, consisting of n lowercase English letters.
# s = collections.deque(input())
# s.appendleft(0)
s = " " + input()

# maxn = 5010
maxn = n + 1

# dp[0]=0,
# dp[p]=min(a+dp[p−1],
#           min(b+dp[k−1] where s[k,p] is a substring of s[1,k−1]))
dp = [0x3f for _ in range(maxn)]
v = [[0 for _c in range(maxn)] for _r in range(maxn)]
Next = [0 for _n in range(maxn)]

# for (int i = 1; i <= n; i++)
# for (int j = i; j <= n; j++) {
for i in range(1, n+1):
    for j in range(i, n+1):
        if s[i] == s[j]:
            v[i][j] = v[i - 1][j - 1] + 1
# for row in v: print(row)

dp[0] = 0
for i in range(1, n+1):
    dp[i] = dp[i - 1] + a
    for j in range(1, i):
        t = min(i - j, v[j][i])
        if t :
            dp[i] = min(dp[i], dp[i - t] + b)

print(dp[n])

