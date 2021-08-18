import sys


def solve(N: int, K: int):
    ans = 0
    for n in range(1, N + 1):
        b = 1
        while n * b < K:
            b <<= 1
        ans += 1 / (b * N)
    return ans


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    print((solve(N, K)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
