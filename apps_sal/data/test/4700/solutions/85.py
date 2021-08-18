import sys
from itertools import chain


def solve(
    N: int, M: int, H: "List[int]", A: "List[int]", B: "List[int]"
):
    ok = [1 for _ in range(N)]
    for a, b in zip(A, B):
        if H[a - 1] <= H[b - 1]:
            ok[a - 1] = 0
        if H[b - 1] <= H[a - 1]:
            ok[b - 1] = 0

    return sum(ok)


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))
    M = int(next(tokens))
    H = [int(next(tokens)) for _ in range(N)]
    A = [int()] * (M)
    B = [int()] * (M)
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    answer = solve(N, M, H, A, B)
    print(answer)


def __starting_point():
    main()


__starting_point()
