
def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    X = [0] * N

    # X1 = S-(X2...XN)になる
    # また、(X1 + X2)//2 = A1 より X1 + X2 = 2*A1
    # なので、 X1 = S - 2(A2+A4+An-1) になる
    S = sum(A)
    X[0] = S - sum(A[1::2]) * 2

    # O(N) で解くために、 Xi+1 = 2*A1 - Xi
    for i in range(N - 1):
        X[i + 1] = 2 * A[i] - X[i]

    print(*X)


def __starting_point():
    resolve()
__starting_point()
