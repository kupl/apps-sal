from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    A = [int(input().strip()) for _ in range(N)]
    return N, A


def solve(N, A, INF=10**9 + 1):
    dp = [INF for i in range(N)]
    for i in range(N):
        a = A[N - i - 1]
        idx = bisect_right(dp, a)
        dp[idx] = a
    return bisect_right(dp, INF - 1)


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print(("%s" % str(outputs)))


__starting_point()
