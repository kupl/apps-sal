import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    S = input()
    N = len(S)
    C = [0] * (N + 1)
    QL = [0] * (N + 1)
    A = [0] * (N + 1)
    QR = [0] * (N + 1)
    for i in range(N):
        if S[i] == 'A':
            A[i + 1] = A[i] + 1
        else:
            A[i + 1] = A[i]
        if S[i] == '?':
            QL[i + 1] = QL[i] + 1
        else:
            QL[i + 1] = QL[i]

    for i in range(N - 1, -1, -1):
        if S[i] == 'C':
            C[i] = C[i + 1] + 1
        else:
            C[i] = C[i + 1]
        if S[i] == '?':
            QR[i] = QR[i + 1] + 1
        else:
            QR[i] = QR[i + 1]

    power3 = [1]
    for i in range(N):
        power3.append(power3[-1] * 3 % MOD)

    ans = 0
    for i in range(N):
        if S[i] in 'AC':
            continue
        choose_A = (A[i] * power3[QL[i]] + (QL[i] > 0) * QL[i] * power3[QL[i] - 1]) % MOD
        choose_B = (C[i + 1] * power3[QR[i + 1]] + (QR[i + 1] > 0) * QR[i + 1] * power3[QR[i + 1] - 1]) % MOD
        ans += choose_A * choose_B % MOD
        ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
