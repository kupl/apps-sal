import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, C: int, x: "List[int]", v: "List[int]"):
    mp1 = [0] * (N + 1)
    mp2 = [0] * (N + 1)
    cum = 0
    for i in range(N):
        cum += v[i]
        mp1[i + 1] = max(mp1[i], cum - x[i])
        mp2[i + 1] = max(mp2[i], cum - x[i] * 2)
    mn1 = [0] * (N + 1)
    mn2 = [0] * (N + 1)
    cum = 0
    for i in reversed(list(range(N))):
        cum += v[i]
        mn1[i] = max(mn1[i + 1], cum - (C - x[i]))
        mn2[i] = max(mn2[i + 1], cum - (C - x[i]) * 2)

    print((max(
        max(mp1[i] + mn2[i] for i in range(N + 1)),
        max(mp2[i] + mn1[i] for i in range(N + 1)),
    )))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    C = int(next(tokens))
    x = [int()] * (N)
    v = [int()] * (N)
    for i in range(N):
        x[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, C, x, v)


def __starting_point():
    main()


__starting_point()
