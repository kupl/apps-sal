import sys
from itertools import chain


def solve(N: int, K: int, H: 'List[int]'):
    H = sorted(H, reverse=True)
    return sum(H[K:])


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))
    K = int(next(tokens))
    H = [int(next(tokens)) for _ in range(N)]
    answer = solve(N, K, H)
    print(answer)


def __starting_point():
    main()


__starting_point()
