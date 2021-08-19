L, A, B, M = list(map(int, input().split()))
K = 19
gap = [-1 for k in range(K)]
for k in range(K):
    tmp = 10**k - A
    if tmp % B == 0:
        gap[k] = -1 + tmp // B
    else:
        gap[k] = tmp // B
    gap[k] = min(L - 1, gap[k])
    gap[k] = max(-1, gap[k])
num = [0 for k in range(K)]
for k in range(1, K):
    # k-1,k
    num[k] = -gap[k - 1] + gap[k]


def matrix(d):
    return [[pow(10, d, M), 1, 0], [0, 1, B], [0, 0, 1]]


def mattime(P, Q):
    R = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                R[i][j] += P[i][k] * Q[k][j]
                R[i][j] %= M
    return R


def matexp(P, n):
    if n == 0:
        return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    elif n % 2 == 0:
        return matexp(mattime(P, P), n // 2)
    else:
        return mattime(P, matexp(mattime(P, P), n // 2))


Mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
for d in range(1, K):
    Mat = mattime(matexp(matrix(d), num[d]), Mat)
print(((A * Mat[0][1] + Mat[0][2]) % M))
