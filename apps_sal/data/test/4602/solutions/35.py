import sys


def solve(N: int, K: int, x: "List[int]"):
    return sum(min(xx, abs(xx - K)) for xx in x) * 2


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    x = [int(next(tokens)) for _ in range(N)]
    print((solve(N, K, x)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
