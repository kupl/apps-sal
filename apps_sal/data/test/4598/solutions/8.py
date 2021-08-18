import sys


def solve(N: int):
    return sum(range(1, N + 1))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    print((solve(N)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
