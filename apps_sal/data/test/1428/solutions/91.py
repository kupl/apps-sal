N, C = map(int, input().split())
D = []
for _ in range(C):
    D.append(list(map(int, input().split())))
c = []
for _ in range(N):
    c.append(list(map(int, input().split())))
colors = [[0]*C for _ in range(3)]
for i in range(N):
    for j in range(N):
        colors[(i+j)%3][c[i][j]-1] += 1
ans = 10**10
for i in range(C):
    for j in range(C):
        if i==j:
            continue
        for k in range(C):
            if j==k or k==i:
                continue
            tmp = 0
            for l in range(C):
                tmp += colors[0][l]*D[l][i]
                tmp += colors[1][l]*D[l][j]
                tmp += colors[2][l]*D[l][k]
            ans = min(ans, tmp)
print(ans)
