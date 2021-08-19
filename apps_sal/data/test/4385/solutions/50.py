import sys


def solve(a: int, b: int, c: int, d: int, e: int, k: int):
    print('Yay!' if e - a <= k else ':(')


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))
    b = int(next(tokens))
    c = int(next(tokens))
    d = int(next(tokens))
    e = int(next(tokens))
    k = int(next(tokens))
    solve(a, b, c, d, e, k)


def __starting_point():
    main()


__starting_point()
