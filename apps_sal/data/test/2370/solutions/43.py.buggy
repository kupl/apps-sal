n = int(input())
INF = float("inf")
g = [[INF] * n for _ in range(n)]
ans = 0
for i in range(n):
    for j, c in enumerate(map(int, input().split())):
        if i != j:
            g[i][j] = c
for i in range(n):
    for j in range(i):
        m = min(a + b for a, b in zip(g[i], g[j]))
        if g[i][j] > m:
            print(-1)
            return
        if g[i][j] < m:
            ans += g[i][j]
print(ans)
