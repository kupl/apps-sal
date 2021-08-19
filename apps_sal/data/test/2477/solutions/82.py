import sys
from itertools import chain


def cut_count(A, m):
    """最長の長さ(切り上げ)がm以下になるような切断回数"""
    total = 0
    for a in A:
        n = (a - 1) // m
        total += n
    return total


def solve(N: int, K: int, A: 'List[int]'):
    r = max(A)
    l = 0
    while l + 1 < r:
        m = (r + l) // 2
        if cut_count(A, m) <= K:
            r = m
        else:
            l = m
    return r


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))
    K = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    answer = solve(N, K, A)
    print(answer)


def __starting_point():
    main()


__starting_point()
