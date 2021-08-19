import sys


def solve(H: int, W: int, c: 'List[List[int]]', A: 'List[List[int]]'):
    import numpy as np
    from scipy.sparse.csgraph import floyd_warshall
    from itertools import chain
    mat = floyd_warshall(np.array(c, dtype=np.int64), directed=True)
    return int(sum((mat[a][1] for a in [x for x in chain.from_iterable(A) if x >= 0])))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))
    W = int(next(tokens))
    c = [[int(next(tokens)) for _ in range(9 - 0 + 1)] for _ in range(9 - 0 + 1)]
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]
    print(solve(H, W, c, A))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
