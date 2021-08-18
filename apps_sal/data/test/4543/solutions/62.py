import sys

YES = "Yes"
NO = "No"


def solve(a: int, b: int):
    c = int(str(a) + str(b))
    for i in range(400):
        if c == i * i:
            print(YES)
            break
    else:
        print(NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))
    b = int(next(tokens))
    solve(a, b)


def __starting_point():
    main()


__starting_point()
