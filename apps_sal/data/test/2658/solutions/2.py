import sys
from itertools import chain


def solve(N: int, K: int, A: "List[int]"):
    M = [-1 for _ in range(N)]
    M[0] = 0
    current = 1
    n = 1
    while n <= K:
        current = A[current - 1]
        if M[current - 1] == -1:
            M[current - 1] = n
        else:
            loop_len = n - M[current - 1]
            rest = K - n
            rest = rest % loop_len
            K = n + rest
        n += 1
    return current


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))
    K = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    answer = solve(N, K, A)
    print(answer)


def __starting_point():
    main()


__starting_point()
