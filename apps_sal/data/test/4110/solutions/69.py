import sys


def solve(D: int, G: int, p: "List[int]", c: "List[int]"):
    from itertools import product, compress
    from math import ceil

    def f():
        for selectors in product([True, False], repeat=D):
            n, g = 0, G
            for i, (pp, cc) in compress(enumerate(zip(p, c), 1), selectors):
                n += pp
                g -= i * 100 * pp + cc
            for i in range(D, 0, -1):
                if selectors[i - 1]:
                    continue
                if g <= 0:
                    break
                nn = min(p[i - 1], ceil(g / i / 100))
                n += nn
                g -= nn * i * 100
            yield n
    return min(f())


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    D = int(next(tokens))
    G = int(next(tokens))
    p = [int()] * (D)
    c = [int()] * (D)
    for i in range(D):
        p[i] = int(next(tokens))
        c[i] = int(next(tokens))
    print((solve(D, G, p, c)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
