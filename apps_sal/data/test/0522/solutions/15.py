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
ans = 1
matrix = [[0] * 3 for i in range(3)]
matrix[0][0] = matrix[0][1] = matrix[0][2] = 1
matrix[1][0] = 1
matrix[2][1] = 1
f_matrix = pow_matrix(matrix, n - 3, MOD - 1)
ans *= pow(f3, f_matrix[0][0], MOD)
ans *= pow(f2, f_matrix[0][1], MOD)
ans *= pow(f1, f_matrix[0][2], MOD)
matrix = [[0] * 5 for i in range(5)]
matrix[0][0] = matrix[0][1] = matrix[0][2] = 1
matrix[0][3] = 2
matrix[0][4] = -6
matrix[1][0] = matrix[2][1] = 1
matrix[3][3] = matrix[3][4] = 1
matrix[4][4] = 1
c_matrix = pow_matrix(matrix, n - 3, MOD - 1)
ans *= pow(c, c_matrix[0][3] * 4 + c_matrix[0][4], MOD)
print(ans % MOD)
