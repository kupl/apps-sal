import sys


def solve(K: int, S: int):
    ans = 0
    for x in range(K + 1):
        for y in range(K + 1):
            if 0 <= S - x - y <= K:
                ans += 1
    return ans


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))
    S = int(next(tokens))
    print((solve(K, S)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
