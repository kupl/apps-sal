import sys


def solve(N: int, M: int):
    if N == 1 and M == 1:
        print(1)
    elif N == 1 or M == 1:
        print(max(N, M) - 2)
    else:
        print(N * M - 2 * N - 2 * M + 4)
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
