#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")

XX = (-2, -2, -2, -1, -1, -1, 0, 0, 0)
YY = (-2, -1, 0, -2, -1, 0, -2, -1, 0)


def solve(H: int, W: int, N: int, a: "List[int]", b: "List[int]"):
    counter = Counter()
    for aa, bb in zip(a, b):
        for x, y in zip(XX, YY):
            if aa+x < 1:
                continue
            elif aa+x+2 > H:
                continue
            elif bb+y < 1:
                continue
            elif bb+y+2 > W:
                continue
            counter[(aa+x, bb+y)] += 1
    ans = [0]*10
    for key, val in counter.items():
        ans[val] += 1

    ans[0] = (H-2)*(W-2) - sum(ans)
    print(*ans, sep="\n")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(H, W, N, a, b)


def __starting_point():
    main()

__starting_point()
