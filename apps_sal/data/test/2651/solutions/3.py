from random import randrange
from itertools import accumulate
from itertools import product, combinations
MOD = 10**9 + 7


def solve(X, Y):
    DX = [a - b for a, b in zip(X[1:], X)]
    DY = [a - b for a, b in zip(Y[1:], Y)]
    a = sum((i + 1) * (len(DX) - i) * dx for i, dx in enumerate(DX))
    b = sum((i + 1) * (len(DY) - i) * dy for i, dy in enumerate(DY))
    return (a * b) % MOD


def naive(X, Y):
    a = 0
    for (x1, x2), (y1, y2) in product(combinations(X, 2), combinations(Y, 2)):
        a += (x2 - x1) * (y2 - y1)
        a %= MOD
    return a


def test():
    for _ in range(10000):
        X = list(accumulate([randrange(1, 8) for _ in range(3)]))
        Y = list(accumulate([randrange(1, 8) for _ in range(2)]))
        a1 = solve(X, Y)
        a2 = naive(X, Y)
        if a1 != a2:
            print((X, Y))
            print(a1)
            print(a2)
            return


def __starting_point():
    N, M = list(map(int, input().split()))
    X = tuple(map(int, input().split()))
    Y = tuple(map(int, input().split()))
    print((solve(X, Y)))


__starting_point()
