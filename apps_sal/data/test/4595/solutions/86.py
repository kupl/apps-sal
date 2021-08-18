import sys


def solve(s: str):
    A = min((i for i, c in enumerate(s) if c == "A"), default=len(s))
    Z = max((i for i, c in enumerate(s) if c == "Z"), default=0)
    return max(0, Z - A + 1)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)
    print((solve(s)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
