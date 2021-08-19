# @author

import sys


class EProductOrientedRecurrence:
    def solve(self):
        MOD = 10 ** 9 + 7
        D = 3
        I = [
            [1 if i == j else 0 for j in range(D)]
            for i in range(D)
        ]

        def mat_mult(A, B):
            n, m, p = len(A), len(A[0]), len(B[0])
            assert (len(B) == m)
            C = [[0] * p for _ in range(n)]
            for i in range(n):
                for k in range(m):
                    Aik = A[i][k]
                    for j in range(p):
                        C[i][j] = (C[i][j] + Aik * B[k][j]) % (MOD - 1)
            return C

        def mat_pow(A, p):
            if p == 0:
                return I
            if p == 1:
                return A
            if p % 2 == 0:
                return mat_pow(mat_mult(A, A), p // 2)
            else:
                return mat_mult(A, mat_pow(A, p - 1))

        n, f1, f2, f3, c = [int(_) for _ in input().split()]
        M = [[0, 1, 0],
             [0, 0, 1],
             [1, 1, 1]]

        Rf1 = mat_mult(mat_pow(M, n - 1), [[1], [0], [0]])[0][0]
        Rf2 = mat_mult(mat_pow(M, n - 1), [[0], [1], [0]])[0][0]
        Rf3 = mat_mult(mat_pow(M, n - 1), [[0], [0], [1]])[0][0]
        Rpower = (mat_mult(mat_pow(M, n - 1), [[1], [2], [3]])[0][0] - n) % (MOD - 1)

        ans = pow(f1, Rf1, MOD) * pow(f2, Rf2, MOD) * pow(f3, Rf3, MOD) * pow(c, Rpower, MOD)
        ans %= MOD
        print(ans)


solver = EProductOrientedRecurrence()
input = sys.stdin.readline

solver.solve()
