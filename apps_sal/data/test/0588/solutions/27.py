import numpy as np
N = int(input())
X = []
Y = []
for _ in range(N):
    (x, y) = map(int, input().split())
    X.append(x)
    Y.append(y)
X = np.array(X)
Y = np.array(Y)
theta = np.arctan2(X, Y)
index = theta.argsort()
X = X[index]
Y = Y[index]
X = np.tile(X, 2)
Y = np.tile(Y, 2)
Xcum = X.cumsum()
Ycum = Y.cumsum()
ans = (Ycum - Ycum[:, None]) ** 2 + (Xcum - Xcum[:, None]) ** 2
m = 0
for i in range(N * 2):
    m = max(m, ans[i, i:i + N + 1].max())
print(m ** 0.5)
