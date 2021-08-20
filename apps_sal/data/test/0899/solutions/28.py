(N, M) = map(int, input().split())
d = [[10 ** 10] * N for i in range(N)]
a = [0] * M
b = [0] * M
c = [0] * M
for i in range(M):
    (a[i], b[i], c[i]) = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
    d[a[i]][b[i]] = c[i]
    d[b[i]][a[i]] = c[i]
for i in range(N):
    d[i][i] = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            d[j][k] = min(d[j][k], d[j][i] + d[i][k])
ans = M
for i in range(M):
    tmp = 0
    for j in range(N):
        if d[j][a[i]] + c[i] == d[j][b[i]]:
            tmp = 1
    ans -= tmp
print(ans)
