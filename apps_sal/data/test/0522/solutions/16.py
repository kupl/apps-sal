def baby_step_giant_step(g, y, p):
    """y = g^x (mod p)を満たすxを求める"""
    m = int(p ** 0.5) + 1
    baby = {}
    b = 1
    for i in range(m):
        baby[b] = i
        b = b * g % p
    gm = pow(b, p - 2, p)
    giant = y
    for i in range(m):
        if giant in baby:
            x = i * m + baby[giant]
            return x
        giant = giant * gm % p
    return -1


def _mul(A, B, MOD):
    C = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for k in range(len(B)):
            for j in range(len(B[0])):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C


def pow_matrix(A, n, MOD):
    """A**nをダブリングによって求める"""
    B = [[0] * len(A) for i in range(len(A))]
    for i in range(len(A)):
        B[i][i] = 1
    while n > 0:
        if n & 1:
            B = _mul(A, B, MOD)
        A = _mul(A, A, MOD)
        n = n // 2
    return B


(n, f1, f2, f3, c) = map(int, input().split())
MOD = 10 ** 9 + 7
log_f1 = baby_step_giant_step(5, f1, MOD)
log_f2 = baby_step_giant_step(5, f2, MOD)
log_f3 = baby_step_giant_step(5, f3, MOD)
log_c = baby_step_giant_step(5, c, MOD)
matrix = [[0] * 5 for i in range(5)]
matrix[0][0] = 1
matrix[0][1] = 1
matrix[0][2] = 1
matrix[0][3] = 2 * log_c
matrix[0][4] = -6 * log_c
matrix[1][0] = 1
matrix[2][1] = 1
matrix[3][3] = 1
matrix[3][4] = 1
matrix[4][4] = 1
matrix_n = pow_matrix(matrix, n - 3, MOD - 1)
ans = log_f3 * matrix_n[0][0] + log_f2 * matrix_n[0][1] + log_f1 * matrix_n[0][2] + 4 * matrix_n[0][3] + matrix_n[0][4]
ans = ans % (MOD - 1)
print(pow(5, ans, MOD))
