import sys


def solve(s: str):
    """
    >>> solve("needed")
    (2, 3)
    >>> solve("ede")
    (1, 3)
    """
    for i, (c0, c1) in enumerate(zip(s, s[1:]), 1):
        if c0 == c1:
            return i, i + 1
    for i, (c0, c2) in enumerate(zip(s, s[2:]), 1):
        if c0 == c2:
            return i, i + 2
    return (-1, -1)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)
    print((*solve(s)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
