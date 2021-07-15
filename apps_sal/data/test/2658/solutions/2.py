#!/usr/bin/env python3
import sys
from itertools import chain


def solve(N: int, K: int, A: "List[int]"):
    M = [-1 for _ in range(N)]
    M[0] = 0
    current = 1
    n = 1
    while n <= K:
        current = A[current - 1]
        if M[current - 1] == -1:  # 一度も通ったことがない
            M[current - 1] = n  # n ステップ目に通った事を記録
        else:
            loop_len = n - M[current - 1]  # ループの長さ
            rest = K - n  # 残り長さ
            rest = rest % loop_len  # 残り長さをループの余剰にする
            K = n + rest
        n += 1
    return current


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
