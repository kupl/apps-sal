import sys


def solve(N: int):
    if N >= 64:
        print(64)
    elif N >= 32:
        print(32)
    elif N >= 16:
        print(16)
    elif N >= 8:
        print(8)
    elif N >= 4:
        print(4)
    elif N >= 2:
        print(2)
    else:
        print(1)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    solve(N)


def __starting_point():
    main()


__starting_point()
