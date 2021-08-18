import heapq
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, a: "List[int]"):
    h = a[:N]
    heapq.heapify(h)
    l1 = [0] * (N + 1)
    l1[0] = sum(h)
    for i in range(N):
        m = heapq.heappushpop(h, a[N + i])
        l1[i + 1] = l1[i] + a[N + i] - m
    h = [-ai for ai in a[-N:]]
    heapq.heapify(h)
    l2 = [0] * (N + 1)
    l2[N] = sum(h)
    for i in reversed(list(range(N))):
        m = heapq.heappushpop(h, -a[N + i])
        l2[i] = l2[i + 1] + (-a[N + i]) - m
    print((max(l1[i] + l2[i] for i in range(N + 1))))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    a = [int(next(tokens)) for _ in range(3 * N)]
    solve(N, a)


def __starting_point():
    main()


__starting_point()
