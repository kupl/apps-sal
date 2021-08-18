import sys


def solve(N: int, L: "List[int]"):
    from itertools import combinations
    from bisect import bisect_left as bl
    L = sorted(L)
    ans = 0
    for ai, a in enumerate(L):
        for bi, b in enumerate(L[ai + 1:-1], ai + 1):
            ci = bl(L, a + b)
            ans += ci - bi - 1
    return ans


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    L = [int(next(tokens)) for _ in range(N)]
    print((solve(N, L)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
