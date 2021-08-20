import sys


def solve(N: int, a: 'List[int]'):
    from collections import Counter
    ans = 0
    for (k, v) in list(Counter(a).items()):
        ans += v - k if v >= k else v
    return ans


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    a = [int(next(tokens)) for _ in range(N)]
    print(solve(N, a))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
