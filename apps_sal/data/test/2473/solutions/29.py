n, k = map(int, input().split())
XY = [[0] * 2 for i in range(n)]
X = [0] * n
Y = [0] * n
Z = [i for i in range(1, n + 1)]
for i in range(n):
    X[i], Y[i] = map(int, input().split())
    XY[i] = [X[i], Y[i]]
X.sort()
Y.sort()
XX = dict(zip(X, Z))
YY = dict(zip(Y, Z))
XXX = dict(zip(Z, X))
YYY = dict(zip(Z, Y))
A = [[0] * n for i in range(n)]
for i in range(n):
    A[XX[XY[i][0]] - 1][YY[XY[i][1]] - 1] += 1
C = [[0] * (n + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        C[i][j] = C[i - 1][j] + C[i][j - 1] - C[i - 1][j - 1] + A[i - 1][j - 1]
ans = 10**20
for i in range(1, n):
    for j in range(i + 1, n + 1):
        for s in range(1, n):
            for t in range(s + 1, n + 1):
                if C[j][t] - C[j][s - 1] - C[i - 1][t] + C[i - 1][s - 1] < k:
                    continue
                a = (XXX[j] - XXX[i]) * (YYY[t] - YYY[s])
                if a < ans:
                    ans = a
print(ans)
