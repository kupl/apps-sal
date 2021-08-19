import sys


def solve(N: int, M: int, P: int, A: 'List[int]', B: 'List[int]', C: 'List[int]'):
    import numpy as np
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import bellman_ford, NegativeCycleError

    def to_csr_matrix(X, Y, Z, shape, dtype):
        d = {}
        for (x, y, z) in zip(X, Y, Z):
            d[x, y] = max(d.get((x, y), -float('inf')), z)
        (ind, data) = list(zip(*list(d.items())))
        return csr_matrix((data, list(zip(*ind))), shape=shape, dtype=dtype)
    smat = bellman_ford(csr_matrix((C, (A, B)), shape=(N + 1, N + 1), dtype=np.int32), directed=True, unweighted=True, indices=1)
    tmat = bellman_ford(csr_matrix((C, (B, A)), shape=(N + 1, N + 1), dtype=np.int32), directed=True, unweighted=True, indices=N)
    r = set([i for (i, v) in enumerate(smat + tmat) if not np.isinf(v)])
    (A, B, C) = list(zip(*[(a, b, c) for (a, b, c) in zip(A, B, C) if b in r]))
    try:
        csr_mat = to_csr_matrix(A, B, C, (N + 1, N + 1), np.float64)
        csr_mat.data = P - csr_mat.data
        return -min(int(bellman_ford(csr_mat, directed=True, indices=1)[N]), 0)
    except NegativeCycleError:
        return -1


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    M = int(next(tokens))
    P = int(next(tokens))
    A = [int()] * M
    B = [int()] * M
    C = [int()] * M
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    print(solve(N, M, P, A, B, C))


def __starting_point():
    main()


__starting_point()
