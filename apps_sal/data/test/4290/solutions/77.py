import sys


def solve(N: int, M: int):
    T = N + M
    T = T * (T - 1) / 2
    return print(int(T - M * N))


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
