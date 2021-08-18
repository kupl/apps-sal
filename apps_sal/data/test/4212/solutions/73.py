import sys
from itertools import chain


def solve(
    N: int, M: int, Q: int, ABCD: "List[(int,int,int,int)]",
):
    def dfs(A, l, r, n):
        if n > 0:
            max_score = 0
            for Ai in range(l, r + 1):
                A.append(Ai)
                score = dfs(A, Ai, r, n - 1)
                if score > max_score:
                    max_score = score
                A.pop()
            return max_score
        else:
            score = 0
            for a, b, c, d in ABCD:
                if A[b - 1] - A[a - 1] == c:
                    score += d
            return score

    return dfs([], 1, M, N)


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))
    M = int(next(tokens))
    Q = int(next(tokens))
    ABCD = []
    for i in range(Q):
        a = int(next(tokens))
        b = int(next(tokens))
        c = int(next(tokens))
        d = int(next(tokens))
        ABCD.append((a, b, c, d))
    answer = solve(N, M, Q, ABCD)
    print(answer)


def __starting_point():
    main()


__starting_point()
