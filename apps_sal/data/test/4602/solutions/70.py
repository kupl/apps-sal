import sys


def solve(N: int, K: int, x: "List[int]"):
    res = 0
    for x_ in x:
        res += 2 * min(x_, abs(K - x_))
    print(res)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    x = [int(next(tokens)) for _ in range(N)]
    solve(N, K, x)


def __starting_point():
    main()


__starting_point()
