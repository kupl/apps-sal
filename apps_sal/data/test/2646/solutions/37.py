
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

G = {i: [] for i in range(1, N + 1)}
seen = [False] * (N + 1)

for a, b in AB:
    G[a].append(b)
    G[b].append(a)

dp = [10 ** 9] * (N + 1)
dp[1] = 0

que = []
que.append(1)
while len(que) > 0:
    q = que.pop(0)
    for g in G[q]:
        if not seen[g]:
            seen[g] = True
            que.append(g)
        dp[g] = min(dp[g], dp[q] + 1)

print("Yes")
for i in range(2, N + 1):
    t = dp[i]
    for g in G[i]:
        if dp[g] < t:
            print(g)
            break
