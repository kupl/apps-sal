W, H, N = list(map(int, input().split()))
X = []
Y = []
A = []
field = [[0] * W for _ in range(H)]
for i in range(N):
    x, y, a = list(map(int, input().split()))
    X.append(x)
    Y.append(y)
    A.append(a)

for i in range(N):
    if A[i] == 1:
        for j in range(X[i]):
            for k in range(H):
                field[k][j] = 1
    elif A[i] == 2:
        for j in range(X[i], W):
            for k in range(H):
                field[k][j] = 1
    elif A[i] == 3:
        for j in range(W):
            for k in range(Y[i]):
                field[k][j] = 1
    else:
        for j in range(W):
            for k in range(Y[i], H):
                field[k][j] = 1

Sum = 0
for i in range(W):
    for j in range(H):
        if field[j][i] == 0:
            Sum += 1

print(Sum)
