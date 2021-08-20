def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    X = [0] * N
    S = sum(A)
    X[0] = S - sum(A[1::2]) * 2
    for i in range(N - 1):
        X[i + 1] = 2 * A[i] - X[i]
    print(*X)


def __starting_point():
    resolve()


__starting_point()
