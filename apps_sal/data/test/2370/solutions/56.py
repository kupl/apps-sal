import sys


def solve(N: int, A: 'List[List[int]]'):
    import numpy as np
    from scipy.sparse.csgraph import floyd_warshall
    A = np.array(A, dtype=np.float64)
    B = floyd_warshall(A, directed=True)
    if not np.array_equal(A, B):
        return -1
    delta = 0.001
    (_, pre) = floyd_warshall(A - delta + np.identity(N) * delta, return_predecessors=True)
    return int(A[pre == [[i] * N for i in range(N)]].sum()) // 2


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]
    print(solve(N, A))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
