import sys


def solve(N: int, A: 'List[List[int]]'):
    from itertools import accumulate
    B = [list(accumulate([0] + a)) for a in A]
    return max((B[0][i + 1] + B[1][N] - B[1][i] for i in range(N)))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(2)]
    print(solve(N, A))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
