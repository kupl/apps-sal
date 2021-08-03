n, m = map(int, input().split())
dis = [[float("inf") for i in range(n)] for j in range(n)]
for i in range(n):
    dis[i][i] = 0
abc = []
for i in range(m):
    a, b, c = map(int, input().split())
    abc.append([a, b, c])
    dis[a - 1][b - 1] = c
    dis[b - 1][a - 1] = c


def warshall_floyd(dis):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dis1 = dis[i][j]
                dis2 = dis[i][k] + dis[k][j]
                dis[i][j] = min(dis1, dis2)
    return dis


data = warshall_floyd(dis)
ans = 0
for i in range(m):
    a, b, c = abc[i][0], abc[i][1], abc[i][2]
    for j in range(n):
        if c + data[b - 1][j] == data[a - 1][j]:
            break
    else:
        ans += 1
print(ans)
