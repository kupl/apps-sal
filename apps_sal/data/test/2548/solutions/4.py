T, = list(map(int, input().split()))
for t in range(T):
    N, = list(map(int, input().split()))
    X = [0] * (N + 1)
    for i, c in enumerate(input().strip()):
        X[i + 1] = X[i] + int(c)
    d = dict()
    for i in range(N + 1):
        x = X[i] - i
        if x not in d:
            d[x] = 0
        d[x] += 1
    R = 0
    for k in d:
        R += d[k] * (d[k] - 1) // 2
    print(R)
