def matrix_product(X, Y, M):
    XY = [[0] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                XY[i][j] += X[i][k] * Y[k][j] % M
            XY[i][j] %= M

    return XY


def power(X, n, M):
    res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    if n == 0:
        return res

    while n > 0:
        if n & 1:
            res = matrix_product(res, X, M)
        X = matrix_product(X, X, M)
        n //= 2

    return res


L, A, B, M = list(map(int, input().split()))

X = [0, A, 1]

for d in range(1, 19):
    if L == 0:
        break

    l = (10**(d - 1) - A + B - 1) // B
    r = (10**d - A) // B
    if (10**d - A) % B == 0:
        r -= 1

    if l < 0:
        l = 0
    if r < 0:
        r = -1

    C = min(r - l + 1, L)
    L -= C

    Y = power([[10**d, 0, 0], [1, 1, 0], [0, B, 1]], C, M)

    next_X = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            next_X[i] += X[j] * Y[j][i] % M
        next_X[i] %= M
    X = next_X

print((X[0]))
