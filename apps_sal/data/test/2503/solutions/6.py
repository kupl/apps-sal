(N, K) = map(int, input().split())
g = [[0] * K for _ in range(K)]
for _ in range(N):
    (x, y, c) = input().split()
    x = int(x)
    y = int(y)
    tmp = (x // K + y // K) % 2
    x %= K
    y %= K
    if tmp == 0 and c == 'B' or (tmp == 1 and c == 'W'):
        g[x][y] += 1
    else:
        g[x][y] -= 1
for i in range(K):
    for j in range(1, K):
        g[i][j] += g[i][j - 1]
for i in range(1, K):
    for j in range(K):
        g[i][j] += g[i - 1][j]
ans = 0
for i in range(K):
    for j in range(K):
        n_satisfied = g[-1][-1] - 2 * (g[-1][j] + g[i][-1]) + 4 * g[i][j]
        ans = max(ans, (N + n_satisfied) // 2, (N - n_satisfied) // 2)
print(ans)
