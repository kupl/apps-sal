import itertools as it
(n, m, r) = map(int, input().split())
ll = list(map(int, input().split()))
d = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(m):
    (a, b, t) = map(int, input().split())
    d[a - 1][b - 1] = t
    d[b - 1][a - 1] = t
for i in range(n):
    d[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
ans = 10 ** 9
for p in it.permutations(ll):
    tmp = 0
    for j in range(r - 1):
        (s, g) = (p[j] - 1, p[j + 1] - 1)
        tmp += d[s][g]
    ans = min(ans, tmp)
print(ans)
