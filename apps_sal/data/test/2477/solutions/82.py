#!/usr/bin/env python3
import sys
from itertools import chain


def cut_count(A, m):
    """最長の長さ(切り上げ)がm以下になるような切断回数"""
    total = 0
    for a in A:
        n = (a - 1) // m
        total += n
    return total


def solve(N: int, K: int, A: "List[int]"):
    r = max(A)
    l = 0
    while l + 1 < r:
        m = (r + l) // 2
        if cut_count(A, m) <= K:
            r = m  # r は K回以下の切断回数で到達できる長さ
        else:
            l = m  # l は K回より多いの切断回数で到達できる長さ
    # print(l, r)
    return r


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # N, K, A = map(int, line.split())
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    answer = solve(N, K, A)
    print(answer)


def __starting_point():
    main()

__starting_point()
