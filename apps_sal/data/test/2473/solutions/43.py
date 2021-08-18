import sys
from itertools import combinations


def _solve(y1, y2, sorted_points, K):
    y1, y2 = tuple(sorted([y1, y2]))
    x = tuple(x for x, y in sorted_points if y1 <= y <= y2)
    if len(x) < K:
        return float('inf')
    return min((y2 - y1) * (x2 - x1) for x1, x2 in zip(x, x[K - 1:]))


def solve(N: int, K: int, x: "List[int]", y: "List[int]"):
    sorted_points = tuple(sorted(zip(x, y)))
    return min(_solve(y1, y2, sorted_points, K) for y1, y2 in combinations(y, 2))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    x = [int()] * (N)
    y = [int()] * (N)
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    print((solve(N, K, x, y)))


def __starting_point():
    main()


__starting_point()
