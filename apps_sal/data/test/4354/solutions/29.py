(n, m) = list(map(int, input().split()))
X = [tuple(map(int, input().split())) for _ in range(n)]
Y = [tuple(map(int, input().split())) for _ in range(m)]
for x in X:
    d1 = sum(x)
    d2 = x[0] - x[1]
    z = 10 ** 9
    for (i, y) in enumerate(Y, 1):
        D1 = sum(y)
        D2 = y[0] - y[1]
        Z = max(abs(D1 - d1), abs(D2 - d2))
        if z > Z:
            z = Z
            ans = i
    print(ans)
