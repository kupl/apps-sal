import sys


def solve(X: int, Y: int):
    return 'Alice' if abs(X - Y) > 1 else 'Brown'


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))
    Y = int(next(tokens))
    print(solve(X, Y))


def __starting_point():
    main()


__starting_point()
