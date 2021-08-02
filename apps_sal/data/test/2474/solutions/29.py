#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int


def solve(N: int, C: "List[int]"):
    pows = [1]
    for i in range(N):
        pows.append(pows[i] * 2 % MOD)

    C.sort(reverse=True)
    ret = 0
    for i, v in enumerate(C):
        if i > 0:
            ret += (pows[i] + pows[i - 1] * i) * (pows[N - i - 1]) * v
        else:
            ret += pows[i] * (pows[N - i - 1]) * v
    ret = ret * pows[N] % MOD
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, C)


def __starting_point():
    main()


__starting_point()
