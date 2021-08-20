import sys


def solve(N: int, M: int, A: 'List[int]'):
    from collections import defaultdict
    acc = [0] * (N + 1)
    for (i, a) in enumerate(A, 1):
        acc[i] = (acc[i - 1] + a) % M
    dp = defaultdict(int)
    ans = 0
    for a in acc:
        ans += dp[a]
        dp[a] += 1
    return ans


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    M = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    print(solve(N, M, A))


def __starting_point():
    main()


__starting_point()
