import sys
from itertools import chain


MOD = 1000000007
OFFSET = 10 ** 100


def k_in_n(k, n):
    """0〜n までの数からちょうど k 個の数を選ぶ時の最大最小"""
    minimum = (k * (k - 1)) // 2
    maximum = (k * (2 * n - k + 1)) // 2
    return (minimum, maximum)


def solve(N: int, K: int):
    keep = None
    answer = 0
    for k in range(K, N + 2):
        if keep is None:
            keep = k_in_n(k, N)
        else:
            minmax = k_in_n(k, N)
            if minmax[0] + OFFSET <= keep[1]:
                keep[0] -= OFFSET
                keep[1] = minimum[1]
            else:
                answer = (answer + keep[1] - keep[0] + 1) % MOD
                keep = minmax

    if keep is not None:
        answer = (answer + keep[1] - keep[0] + 1) % MOD
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))
    K = int(next(tokens))
    answer = solve(N, K)
    print(answer)


def __starting_point():
    main()


__starting_point()
