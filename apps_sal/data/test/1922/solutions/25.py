import sys


def solve(N: int, M: int):
    N, M = min(N, M), max(N, M)

    if N == 1 and M == 1:
        print((1))
        return

    if N == 1:
        print((M - 2))
        return

    ans = (N - 2) * (M - 2)
    print(ans)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    M = int(next(tokens))
    solve(N, M)


def __starting_point():
    main()


__starting_point()
