import sys
from itertools import accumulate
from collections import Counter
INF = float("inf")


def solve(N: int, K: int, A: "List[int]"):

    ans = 0

    acc = [0] + list(accumulate(A))

    cnt = Counter()
    for j in range(1, N + 1):
        if j - 1 >= 0:
            cnt[(acc[j - 1] - (j - 1)) % K] += 1

        if j - K >= 0:
            cnt[(acc[j - K] - (j - K)) % K] -= 1

        ans += cnt[(acc[j] - j) % K]
    print(ans)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    solve(N, K, A)


def __starting_point():
    main()


__starting_point()
