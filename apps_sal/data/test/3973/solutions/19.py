mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    imos = [0] * M
    imos_2 = [0] * M
    B = [0] * M
    base = 0
    for i in range(1, N):
        if A[i] > A[i-1]:
            k = A[i] - A[i - 1]
            base += k
            if k == 1:
                continue
            if A[i] + 1 < M:
                imos_2[A[i] + 1] += k
            if A[i] + 2 < M:
                imos_2[A[i] + 2] += -(k-1)
            imos_2[A[i - 1] + 2] += -1
        else:
            k = A[i] - A[i-1] + M
            base += k
            if k == 1:
                continue
            if A[i-1] == M-1:
                imos_2[1] += -1
                imos_2[A[i] + 1] += k
                if A[i] + 2 < M:
                    imos_2[A[i] + 2] += -(k-1)
            else:
                imos_2[(A[i] + 2)%M] += -(k-1)
                imos_2[(A[i] + 1)%M] += k
                imos_2[(A[i - 1] + 2) % M] += -1
                if A[i - 1] + 2 < M:
                    B[0] += -(M - (A[i-1] + 2))
                    imos_2[0] += -1
    for i in range(M):
        if i == 0:
            imos[i] += imos_2[i]
        else:
            imos[i] += imos[i-1] + imos_2[i]
        if i == 0:
            B[i] = B[i] + imos[i]
        else:
            B[i] = B[i-1] + imos[i]
    print((min(B) + base))


def __starting_point():
    main()

__starting_point()
