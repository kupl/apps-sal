def productMatrix(N, A, B):
    Ret = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                Ret[i][j] += A[i][k] * B[k][j]
    return Ret


def modMatrix(N, A, Q):
    for i in range(N):
        for j in range(N):
            A[i][j] %= Q
    return


def powOfMatrix(N, X, n, Q):
    Ret = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    power = '{:060b}'.format(n)[::-1]
    for p in power:
        if p == "1":
            Ret = productMatrix(N, Ret, X)
            modMatrix(N, Ret, Q)
        X = productMatrix(N, X, X)
        modMatrix(N, X, Q)
    return Ret


def main():
    L, A, B, M = list(map(int, input().split()))
    s = A
    ANS = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for i in range(1, 37):
        if s >= pow(10, i):
            continue
        P = [[pow(10, i, M), 0, 0], [1, 1, 0], [0, B, 1]]
        step = (pow(10, i) - s + B - 1) // B
        if L <= step:
            ANS = productMatrix(3, ANS, powOfMatrix(3, P, L, M))
            modMatrix(3, ANS, M)
            break
        ANS = productMatrix(3, ANS, powOfMatrix(3, P, step, M))
        modMatrix(3, ANS, M)
        L -= step
        s += step * B
    print(((ANS[1][0] * A + ANS[2][0]) % M))


def __starting_point():
    main()


__starting_point()
