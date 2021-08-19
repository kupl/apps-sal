(n, m) = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
x = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
d = dict()
for j in l:
    d[x[j]] = j
INF = float('inf')
dp = [-INF for i in range(n + 1)]
dp[0] = 0
l = d.keys()
for i in range(2, n + 1):
    for j in d.keys():
        if j <= i:
            dp[i] = max(dp[i], dp[i - j] * 10 + d[j])
print(dp[n])
