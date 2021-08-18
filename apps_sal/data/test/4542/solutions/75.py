import sys


def solve(S: str):
    from itertools import groupby
    return len(list(groupby(S))) - 1


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)
    print((solve(S)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
