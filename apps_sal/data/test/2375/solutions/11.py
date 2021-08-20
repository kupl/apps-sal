import sys


def solve(X: int, Y: int):
    print('Brown' if -1 <= X - Y <= 1 else 'Alice')


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))
    Y = int(next(tokens))
    solve(X, Y)


def __starting_point():
    main()


__starting_point()
