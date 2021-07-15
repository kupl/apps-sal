import os
import sys


def solve(xs, m):
    xs = [(0, 0)] + xs
    dp = [0] * (m + 1)
    for i in range(1, m + 1):
        dp[i] = dp[i - 1] + 1
        for idx, (x, s) in enumerate(xs):
            if x - s <= i <= x + s:
                dp[i] = dp[i - 1]
                break

            if x + s < i:
                c = i - x - s
                dp[i] = min(c + dp[max(x - c - s - 1, 0)], dp[i])

    return dp[-1]


def pp(input):
    n, m = list(map(int, input().split()))
    xs = [tuple(map(int, input().split())) for _ in range(n)]
    print(solve(xs, m))


if "paalto" in os.getcwd():
    from string_source import string_source

    pp(
        string_source(
            """2 50
20 0
3 1
"""
        )
    )

    pp(
        string_source(
            """3 595
43 2
300 4
554 10
"""
        )
    )

    pp(
        string_source(
            """1 1
1 1
"""
        )
    )

    pp(
        string_source(
            """5 240
13 0
50 25
60 5
155 70
165 70
"""
        )
    )

else:
    pp(sys.stdin.readline)

