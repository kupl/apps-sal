import sys


def solve(W: int, a: int, b: int):
    if abs(a - b) <= W:
        return 0
    return abs(a - b) - W


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))
    a = int(next(tokens))
    b = int(next(tokens))
    print(solve(W, a, b))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
