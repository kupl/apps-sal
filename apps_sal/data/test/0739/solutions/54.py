import sys
sys.setrecursionlimit(100000000)


def mult(A, B, mod):
    D = [[A[0][0] * B[0][0] % mod, 0, 0], [0, 1, 0], [0, 0, 1]]
    D[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod
    D[2][0] = (A[2][0] * B[0][0] + A[2][1] * B[1][0] + A[2][2] * B[2][0]) % mod
    D[2][1] = (A[2][1] * B[1][1] + A[2][2] * B[2][1]) % mod
    return D


def double(C, mod):
    D = [[pow(C[0][0], 2, mod), 0, 0], [(C[1][0] * C[0][0] + C[1][0]) % mod, 1, 0], [(C[2][0] * C[0][0] + C[2][1] * C[1][0] + C[2][0]) % mod, C[2][1] * 2 % mod, 1]]
    return D


def Cpow(C, n, mod):
    if n == 1:
        return C
    else:
        D = double(C, mod)
        if n % 2 == 0:
            return Cpow(D, n // 2, mod)
        else:
            return mult(Cpow(D, n // 2, mod), C, mod)


def solve():
    (L, a, b, M) = map(int, input().split())
    X = 0
    s = a
    nd = -1
    ne = 0
    for d in range(1, 19):
        ne = min((pow(10, d) - a - 1) // b, L - 1)
        if ne < 0:
            continue
        elif ne == nd:
            continue
        C = [[pow(10, d, M), 0, 0], [1, 1, 0], [0, b % M, 1]]
        D = Cpow(C, ne - nd, M)
        X = (X * D[0][0] + D[1][0] * s + D[2][0]) % M
        s += D[2][1]
        if ne == L - 1:
            break
        nd = ne
    print(X)
    return


def __starting_point():
    solve()


__starting_point()
