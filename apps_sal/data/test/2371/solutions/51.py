import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, Z: int, W: int, a: "List[int]"):
    dp = [(0, 0)] * N
    if N == 1:
        dp[N - 1] = (abs(a[N - 1] - W), abs(Z - a[N - 1]))
    else:
        dp[N - 1] = (abs(a[N - 1] - a[N - 2]), abs(a[N - 2] - a[N - 1]))
    for i in reversed(list(range(N - 1))):
        v1 = max(dp[j][1] for j in range(i + 1, N))
        if i == 0:
            v1 = max(v1, abs(a[N - 1] - W))
        else:
            v1 = max(v1, abs(a[N - 1] - a[i - 1]))
        v2 = min(dp[j][0] for j in range(i + 1, N))
        if i == 0:
            v2 = min(v2, abs(Z - a[N - 1]))
        else:
            v2 = min(v2, abs(a[i - 1] - a[N - 1]))
        dp[i] = (v1, v2)
    print((dp[0][0]))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    Z = int(next(tokens))
    W = int(next(tokens))
    a = [int(next(tokens)) for _ in range(N)]
    solve(N, Z, W, a)


def __starting_point():
    main()


__starting_point()
