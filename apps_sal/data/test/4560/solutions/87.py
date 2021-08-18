import sys

YES = "Yes"
NO = "No"


def solve(N: int, A: int):
    return YES if (N % 500) <= A else NO


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    A = int(next(tokens))
    print((solve(N, A)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
