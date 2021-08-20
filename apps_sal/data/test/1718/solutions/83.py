import os
import sys


def main():
    (N, K) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A_min = min(A)
    cnt = 0
    for i in range(0, N - 1, K - 1):
        cnt += 1
    print(cnt)


def __starting_point():
    main()


__starting_point()
