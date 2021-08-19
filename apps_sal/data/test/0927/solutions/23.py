#!/usr/bin/env python3
import sys
try:
    from typing import Dict, List
except ImportError:
    pass


def solve(N: int, M: int, A: "List[int]"):
    mn = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        m = -1
        for Ai in A:
            if i - mn[Ai] >= 0 and dp[i - mn[Ai]] >= 0:
                m = max(m, dp[i - mn[Ai]] + 1)
        if m >= 0:
            dp[i] = m
    assert dp[N] >= 0
    k = N
    res = []  # type: List[int]
    while dp[k]:
        for Ai in A:
            if k - mn[Ai] >= 0 and dp[k - mn[Ai]] == dp[k] - 1:
                res.append(Ai)
                k -= mn[Ai]
                break

    print(("".join(str(d) for d in res)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, A)


def __starting_point():
    main()


__starting_point()
