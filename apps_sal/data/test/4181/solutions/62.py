

import os
import sys


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if A[i] >= B[i]:
            ans += B[i]
            A[i] -= B[i]
        elif A[i] < B[i] and A[i + 1] < B[i] - A[i]:
            ans += A[i + 1] + A[i]
            A[i + 1] = 0
            A[i] = 0
        elif A[i] < B[i] and A[i + 1] >= B[i] - A[i]:
            ans += B[i]
            A[i + 1] -= B[i] - A[i]
            A[i] = 0
    print(ans)


def __starting_point():
    main()


__starting_point()
