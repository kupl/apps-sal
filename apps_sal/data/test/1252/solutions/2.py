n, m, T = map(int, input().split())
adj = [[] for _ in range(n + 1)]
ad_w = [[] for _ in range(n + 1)]
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
pv = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    a, b, t = map(int, input().split())
    adj[b].append(a)
    ad_w[b].append(t)
    if a == 1:
        dp[b][2] = t
        pv[b][2] = 1

for c in range(3, n + 1):
    for v in range(2, n + 1):
        for i, nx in enumerate(adj[v]):
            if dp[nx][c - 1]:
                newdistance = dp[nx][c - 1] + ad_w[v][i]
                if newdistance <= T and (not dp[v][c] or newdistance < dp[v][c]):
                    dp[v][c] = newdistance
                    pv[v][c] = nx


for last in range(n, 0, -1):
    if pv[n][last]:
        break


path = [n]
while pv[path[-1]][last] != 1:
    path.append(pv[path[-1]][last])
    last -= 1

path.append(1)
path.reverse()

print(len(path))
print(' '.join(map(str, path)))
