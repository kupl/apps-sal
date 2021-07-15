N, M = list(map(int,input().split()))
E = set()
d = [[10**9]*N for k in range(N)]
for k in range(N):
    d[k][k] = 0
for k in range(M):
    a, b, c = list(map(int,input().split()))
    E.add((a-1,b-1,c))
    d[a-1][b-1] = c
    d[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
ans = 0
for e in E:
    if d[e[0]][e[1]] != e[2]:
        ans += 1
print(ans)

