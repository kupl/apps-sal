import sys


def solve(N: int, a: "List[int]"):
    ans = float("inf")
    for m in range(-100, 101):
        ans = min(ans,
                  sum((aa - m)**2 for aa in a))
    return ans


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    a = [int(next(tokens)) for _ in range(N)]
    print((solve(N, a)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
