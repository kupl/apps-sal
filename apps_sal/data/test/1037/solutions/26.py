import sys


def solve(N: int, A: "List[int]"):
    A = sorted(enumerate(A), reverse=True, key=lambda x: x[1])

    dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
    for i in range(N):
        for j in range(0, N - i):
            idx, a = A[i + j]
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + a * abs(idx - i))
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + a * abs(N - 1 - j - idx))
    result = -1
    for i in range(N):
        tmp = dp[i][N - i]
        if tmp > result:
            result = tmp
    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    solve(N, A)


def __starting_point():
    main()


__starting_point()
