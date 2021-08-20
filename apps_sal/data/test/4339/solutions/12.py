import sys
from bisect import bisect, bisect_left


def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    C = [A[i] - B[i] for i in range(N)]
    C.sort()
    count = 0
    for (i, c) in enumerate(C):
        least = bisect(C, -c)
        count += N - max(least, i + 1)
    print(count)
    return 0


def __starting_point():
    solve()


__starting_point()
