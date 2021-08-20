(N, A, B) = map(int, input().split())
M = 10 ** 9 + 7


def cmb(N, R, M):
    C = [1] * (R + 1)
    for i in range(1, R + 1):
        C[i] = C[i - 1] * (N + 1 - i) * pow(i, M - 2, M) % M
    return C


C = cmb(N, B, M)
ans = pow(2, N, M) - 1
ans -= C[A] + C[B]
print(ans % M)
