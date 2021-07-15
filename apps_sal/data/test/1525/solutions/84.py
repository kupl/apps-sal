#!/usr/bin/env python3
from itertools import product
import sys

try:
    from typing import List, Tuple
except ImportError:
    pass


MOD = 1000000007  # type: int


def isvalid(ptn: "Tuple[bool]"):
    return not any(h1 and h2 for h1, h2 in zip(ptn, ptn[1:]))


def solve(H: int, W: int, K: int):
    validptns = [
        ptn
        for ptn in product((False, True), repeat=W - 1)
        if isvalid(ptn)
    ]  # type: List[Tuple[bool]]
    dp = [1 if i == K - 1 else 0 for i in range(W)]  # type: List[int]
    for _ in range(H):
        newdp = [0] * W  # type: List[int]
        for ptn in validptns:
            for s in range(W):
                t = s
                if s < W - 1 and ptn[s]:
                    t = s + 1
                elif s > 0 and ptn[s - 1]:
                    t = s - 1
                newdp[t] += dp[s]
                newdp[t] %= MOD
        dp = newdp

    print((dp[0]))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(H, W, K)


def __starting_point():
    main()

__starting_point()
