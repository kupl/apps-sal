import sys


def solve(N: int, K: int):
    e = sum((i % K != 0 and i * 2 % K == 0 for i in range(1, N + 1)))
    z = sum((i % K == 0 for i in range(1, N + 1)))
    return pow(e, 3) + pow(z, 3)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    print(solve(N, K))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
