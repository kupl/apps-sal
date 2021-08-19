def mat_prod(A, B, m):
    x = len(A)
    y = len(B)
    z = len(B[0])
    C = [[0] * z for _ in range(x)]
    for i in range(x):
        for j in range(y):
            for k in range(z):
                C[i][k] += A[i][j] * B[j][k]
                C[i][k] %= m
    return C


def mat_pow(A, n, m):
    if n == 1:
        return A
    if n % 2:
        return mat_prod(mat_pow(A, n - 1, m), A, m)
    B = mat_pow(A, n // 2, m)
    return mat_prod(B, B, m)


(L, a, b, m) = map(int, input().split())
ans = 0
s = a
for k in range(1, 19):
    l = (10 ** (k - 1) - a + b - 1) // b
    r = (10 ** k - a + b - 1) // b
    l = max(l, 0)
    r = min(r, L)
    if l >= r:
        continue
    d = r - l
    X = [[ans, s, 1]]
    Y = [[pow(10, k, m), 0, 0], [1, 1, 0], [0, b, 1]]
    Z = mat_prod(X, mat_pow(Y, d, m), m)
    (ans, s) = Z[0][:2]
print(ans)
