from sys import stdin
n, m = list(map(int, stdin.readline().strip().split()))
adj = [[0, 0] for i in range(max(m, n) + 1)]
dp = [0 for i in range(max(m, n) + 1)]
s = []
for i in range(n):
    a, b = list(map(int, stdin.readline().strip().split()))
    s.append([b, a])
s.sort(reverse=True)
ans = 0
for i in range(n):
    a, b = s[i][1], s[i][0]
    adj[a][0] += 1
    adj[a][1] += b
    dp[adj[a][0]] = max(dp[adj[a][0]] + adj[a][1], dp[adj[a][0]])
print(max(dp))
