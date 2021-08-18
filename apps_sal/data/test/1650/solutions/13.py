import sys
sys.setrecursionlimit(200000)

MOD = 1000000007


def h(L, i):
    return pow(3, len(L) - i, MOD)


def g(L, i):
    if len(L) == i:
        return 1
    if L[i] == '1':
        return ((2 * g(L, i + 1)) % MOD + h(L, i + 1)) % MOD
    return g(L, i + 1)


def solve(L: str):
    return g(L, 0)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = next(tokens)
    print((solve(L)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
