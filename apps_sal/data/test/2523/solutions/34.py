import sys


def solve(S: str):
    N = len(S)
    m = N
    for i in range(N - 1):
        if S[i] != S[i + 1]:
            m = min(m, max(N - (i + 1), i + 1))
    print(m)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)
    solve(S)


def __starting_point():
    main()


__starting_point()
