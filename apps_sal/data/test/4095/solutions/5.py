import sys
n, m = list(map(int, input().split()))
s = list(map(int, input().split()))
try:
    ind = s.index(m)
except:
    print(0)
    return
dp = [0 for i in range(n)]
for i in range(ind + 1, n):
    if s[i] < m:
        dp[i] = dp[i - 1] - 1
    elif s[i] > m:
        dp[i] = dp[i - 1] + 1
for i in range(ind - 1, -1, -1):
    if s[i] < m:
        dp[i] = dp[i + 1] - 1
    elif s[i] > m:
        dp[i] = dp[i + 1] + 1
d = dict()
for i in range(ind + 1, n):
    try:
        d[dp[i]] += 1
    except:
        d.update({dp[i]: 1})

ans = 0
for i in range(ind + 1):
    x = -dp[i]
    try:
        ans += d[x]
    except:
        True
    try:
        ans += d[x + 1]
    except:
        True
    if dp[i] == 0 or dp[i] == 1:
        ans += 1
print(ans)
