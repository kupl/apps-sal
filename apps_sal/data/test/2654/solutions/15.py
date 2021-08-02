import sys

import bisect


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    pass
    A.sort()
    B.sort()
    if N % 2 == 0:
        n = N // 2
        mini = (A[n] + A[n - 1]) / 2
        maxi = (B[n] + B[n - 1]) / 2
        print((int((maxi - mini) * 2) + 1))
    else:
        n = N // 2
        mini = A[n]
        maxi = B[n]
        print((maxi - mini + 1))


def __starting_point():
    main()


__starting_point()
