import sys


def solve(N: int, A: 'List[int]'):
    from collections import Counter
    return sum([x % 2 == 1 for x in list(Counter(A).values())])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    print(solve(N, A))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
