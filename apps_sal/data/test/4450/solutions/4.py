import sys
input = sys.stdin.readline
(N, M, K) = list(map(int, input().split()))
X = []
for _ in range(M):
    (x, y, w) = list(map(int, input().split()))
    X.append([min(x, y), max(x, y), w])
X = (sorted(X, key=lambda x: x[2]) + [[0, 0, 10 ** 20] for _ in range(K)])[:K]
D = {}
for (x, y, w) in X:
    if x:
        D[x * 10 ** 6 + y] = w
flg = 1
while flg:
    flg = 0
    for i in range(len(X)):
        (x1, y1, w1) = X[i]
        for j in range(i + 1, len(X)):
            (x2, y2, w2) = X[j]
            if x1 == x2:
                (a, b) = (min(y1, y2), max(y1, y2))
            elif y1 == y2:
                (a, b) = (min(x1, x2), max(x1, x2))
            elif x1 == y2:
                (a, b) = (x2, y1)
            elif x2 == y1:
                (a, b) = (x1, y2)
            else:
                (a, b) = (0, 0)
            if a:
                if a * 10 ** 6 + b in D and w1 + w2 < D[a * 10 ** 6 + b] or (a * 10 ** 6 + b not in D and w1 + w2 < X[-1][2]):
                    if a * 10 ** 6 + b in D:
                        for k in range(len(X)):
                            if X[k][0] == a and X[k][1] == b:
                                X[k][2] = w1 + w2
                    else:
                        (x, y, w) = X.pop()
                        if x:
                            D.pop(x * 10 ** 6 + y)
                        X.append([a, b, w1 + w2])
                    D[a * 10 ** 6 + b] = w1 + w2
                    X = sorted(X, key=lambda x: x[2])
                    flg = 1
print(X[-1][2])
