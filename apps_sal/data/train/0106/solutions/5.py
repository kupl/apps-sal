T = int(input())

for i in range(T):
    n = int(input())
    X = []
    for j in range(n):
        l, r = list(map(int, input().split()))
        X.append([j, l, r])

    X = sorted(X, key=lambda x: x[1])
    # print(X)

    Y = ["2"] * n
    s = -1
    rmax = X[0][2]
    Y[X[0][0]] = "1"
    for i in range(1, n):
        if X[i][1] > rmax:
            s = i
            break
        rmax = max(rmax, X[i][2])
        Y[X[i][0]] = "1"

    if s < 0:
        print(-1)
    else:
        print(" ".join(Y))
