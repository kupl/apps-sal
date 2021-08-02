L, A, B, M = map(int, input().split())
ans = 0
d = 0


def mul(X, Y):
    Z = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for i in range(3):
        for j in range(3):
            r = 0
            for k in range(3):
                r += X[i][k] * Y[k][j]
            Z[i][j] = r % M
    return Z


x = 0; a = A
while 1:
    kd0 = max(min((10**d - A + B - 1) // B, L), 0)
    kd1 = max(min((10**(d + 1) - A + B - 1) // B, L), 0)

    Q = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    P = [[10**(d + 1), 0, 0], [1, 1, 0], [0, B, 1]]
    k = kd1 - kd0
    while k:
        if k & 1:
            Q = mul(P, Q)
        P = mul(P, P)
        k >>= 1
    x, a = (x * Q[0][0] + a * Q[1][0] + Q[2][0]) % M, (x * Q[0][1] + a * Q[1][1] + Q[2][1]) % M
    if kd1 == L:
        break
    d += 1
print(x)
