import sys


def solve(N: int, M: int, R: int, r: "List[int]", A: "List[int]", B: "List[int]", C: "List[int]"):
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import floyd_warshall
    from itertools import permutations
    from functools import reduce
    mat = floyd_warshall(coo_matrix((C, (A, B)), shape=(N + 1, N + 1)).tocsr(), directed=False)
    def f(a, b): return (a[0] + mat[a[1]][b], b)
    return int(min(reduce(f, q, (0, s))[0] for s, *q in permutations(r)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    M = int(next(tokens))
    R = int(next(tokens))
    r = [int(next(tokens)) for _ in range(R)]
    A = [int()] * (M)
    B = [int()] * (M)
    C = [int()] * (M)
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    print(solve(N, M, R, r, A, B, C))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
