import sys


def solve(S_A: str, S_B: str, S_C: str):
    d = dict(list(zip('abc', list(map(iter, [S_A, S_B, S_C])))))
    try:
        u = 'a'
        while True:
            u = next(d[u])
    except StopIteration:
        return u.upper()


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S_A = next(tokens)
    S_B = next(tokens)
    S_C = next(tokens)
    print(solve(S_A, S_B, S_C))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
