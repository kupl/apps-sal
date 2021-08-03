import sys
from bisect import bisect_right

input = sys.stdin.readline


def main():
    N = int(input())
    A = [0] * N
    for i in range(N):
        A[i] = int(input())

    A = [-a for a in A]

    colors = []
    for a in A:
        idx = bisect_right(colors, a)
        if idx == len(colors):
            colors.append(a)
        else:
            colors[idx] = a

    ans = len(colors)
    print(ans)


def __starting_point():
    main()


__starting_point()
