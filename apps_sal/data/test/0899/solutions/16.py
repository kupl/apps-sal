import sys


def solve(N: int, M: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    import numpy as np
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import floyd_warshall
    omat = csr_matrix((c, (a, b)), shape=(N + 1, N + 1), dtype=np.int32)
    smat = floyd_warshall(omat, directed=False)
    return ((smat - omat) < 0).sum()


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    M = int(next(tokens))
    a = [int()] * (M)
    b = [int()] * (M)
    c = [int()] * (M)
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    print((solve(N, M, a, b, c)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
