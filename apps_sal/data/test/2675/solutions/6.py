n, m = map(int, input().split())
X = {}
Y = {}
for i in range(n):
    x, u = map(int, input().split())
    xu = x * u
    if xu in X:
        X[xu] = X[xu] + 1
    else:
        X[xu] = 1


for i in range(m):
    y, v = map(int, input().split())
    yv = y * v
    if yv in Y:
        Y[yv] = Y[yv] + 1
    else:
        Y[yv] = 1

coll = 0

for i in X:
    if i in Y:
        m = min(X[i], Y[i])
        coll = coll + m
print(coll)
