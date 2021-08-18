import sys

YES = "Yes"
NO = "No"


def solve(A: "List[List[int]]", N: int, b: "List[int]"):
    A_ = []
    for a_ in A:
        A_ += [[a__, False] for a__ in a_]
    for b_ in b:
        for a__ in A_:
            if a__[0] == b_:
                a__[1] = True
    if (A_[0][1] and ((A_[1][1] and A_[2][1]) or
                      (A_[3][1] and A_[6][1])
                      or (A_[4][1] and A_[8][1]))) or \
            (A_[1][1] and A_[4][1] and A_[7][1]) or \
            (A_[2][1] and A_[5][1] and A_[8][1]) or \
            (A_[3][1] and A_[4][1] and A_[5][1]) or \
            (A_[6][1] and A_[7][1] and A_[8][1]) or \
            (A_[2][1] and A_[4][1] and A_[6][1]):
        print(YES)
    else:
        print(NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]
    N = int(next(tokens))
    b = [int(next(tokens)) for _ in range(N)]
    solve(A, N, b)


def __starting_point():
    main()


__starting_point()
