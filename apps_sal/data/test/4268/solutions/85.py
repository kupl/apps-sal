import numpy as np
(N, D) = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))
dis = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        for k in range(D):
            dis[i][j] += (X[i][k] - X[j][k]) ** 2
dot = 0
for i in range(N):
    for j in range(i, N):
        dis[i][j] = np.sqrt(dis[i][j])
        if dis[i][j].is_integer() and dis[i][j] != 0:
            dot += 1
print(dot)
