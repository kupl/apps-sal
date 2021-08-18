import sys


def solve(N: int, M: int, L: int, A: "List[int]", B: "List[int]", C: "List[int]", Q: int, s: "List[int]", t: "List[int]"):
    import numpy as np
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import floyd_warshall
    from itertools import filterfalse
    mat = floyd_warshall(coo_matrix((C, (A, B)), shape=(N + 1, N + 1), dtype=np.int32).tocsr(), directed=False)
    mat = floyd_warshall(mat <= L, directed=False)
    for ss, tt in zip(s, t):
        yield -1 if np.isinf(mat[ss][tt]) else int(mat[ss][tt]) - 1


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    M = int(next(tokens))
    L = int(next(tokens))
    A = [int()] * (M)
    B = [int()] * (M)
    C = [int()] * (M)
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    Q = int(next(tokens))
    s = [int()] * (Q)
    t = [int()] * (Q)
    for i in range(Q):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
    print(*solve(N, M, L, A, B, C, Q, s, t), sep="\n")


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
