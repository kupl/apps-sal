MOD = int(1e9 + 7)


def matMOD(A):
    def f(x): return x % (MOD - 1)
    ret = [list(map(f, i)) for i in A]
    return ret


def matmul(A, B):
    a, b = len(A), len(A[0])
    c = len(B[0])
    ret = [[0] * c for i in range(a)]

    for i in range(a):
        for j in range(c):
            for k in range(b):
                ret[i][j] += A[i][k] * B[k][j]

    return ret


def matmul_log(A, m):
    if m == 1:
        return A

    B = matmul_log(A, m // 2)
    if m % 2 == 0:
        return matMOD(matmul(B, B))

    else:
        return matMOD(matmul(A, matmul(B, B)))


n, f1, f2, f3, c = map(int, input().split())

ini = [
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [4, 2, 0, 0, 0, 2]
]

m = [
    [0, 0, 0, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1]
]

m2 = [
    [1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1]
]


M = matmul_log(m, n - 1)
M2 = matmul_log(m2, n - 1)

x, y, z = matmul([ini[0]], M)[0][0], matmul([ini[1]], M)[0][0], matmul([ini[2]], M)[0][0]
w = matmul([ini[3]], M2)[0][2]

ans = (pow(c, w, MOD) * pow(f1, x, MOD) * pow(f2, y, MOD) * pow(f3, z, MOD)) % MOD
print(ans)
