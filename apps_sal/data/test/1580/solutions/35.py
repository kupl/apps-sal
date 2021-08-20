import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input():
    return sys.stdin.readline().strip()


def resolve():
    from scipy.sparse.csgraph import connected_components
    from scipy.sparse import csr_matrix
    (N, M) = map(int, input().split())
    (A, B, C) = ([0] * M, [0] * M, [1] * M)
    for i in range(M):
        (A[i], B[i], _) = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    csr = csr_matrix((C, (A, B)), shape=(N, N))
    (n, labels) = connected_components(csr)
    print(n)


resolve()
