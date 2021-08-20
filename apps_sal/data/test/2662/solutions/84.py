import sys
from bisect import bisect_left, insort_right
input = sys.stdin.readline


def main():
    N = int(input())
    A = [0] * N
    for i in range(N):
        A[i] = int(input())
    colors = []
    for a in A:
        idx = bisect_left(colors, a)
        if idx != 0:
            colors.pop(idx - 1)
        insort_right(colors, a)
    ans = len(colors)
    print(ans)


def __starting_point():
    main()


__starting_point()
