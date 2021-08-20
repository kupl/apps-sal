import sys


def solve(N: int, A: 'List[int]'):
    dp = [[float('inf')] * N for _ in range(2)]
    dp[0][0] = A[0]
    dp[1][0] = -A[0]
    for (i, a) in enumerate(A[1:], 1):
        dp[0][i] = max(dp[0][i - 1] + a, dp[1][i - 1] - a)
        dp[1][i] = max(dp[0][i - 1] - a, dp[1][i - 1] + a)
    return max(dp[0][N - 2] + A[-1], dp[1][N - 2] - A[-1])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    print(solve(N, A))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
