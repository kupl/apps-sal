import sys


def solve(S: str):
    S = [s1 for (s0, s1) in zip(S, S[1:] + '.') if s0 != s1]
    return len(S) - 1


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)
    print(solve(S))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
