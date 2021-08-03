maxn = int(75)
nvc = int(-100000005)
G = [[nvc for _ in range(maxn)] for _ in range(maxn)]
F = [[nvc for _ in range(maxn)] for _ in range(maxn)]
a = [0 for _ in range(maxn)]
n, m, k = list(map(int, input().split(' ')))
F[0][0] = 0
for i in range(n):
    a = list(map(int, input().split(' ')))
    for u in range(m // 2 + 1):
        for v in range(k):
            G[0][v] = max(G[0][v], F[u][v])
    F = [[nvc for _ in range(maxn)] for _ in range(maxn)]
    for j in range(m):
        for u in range(m // 2 + 1):
            for v in range(k):
                F[u + 1][(v + a[j]) % k] = max(F[u + 1][(v + a[j]) % k], G[u][v] + a[j])
                F[u][v] = max(F[u][v], G[u][v])
        for u in range(m // 2 + 1):
            for v in range(k):
                G[u][v] = F[u][v]
res = 0
for i in range((m // 2) + 1):
    res = max(res, F[i][0])
print(res)
