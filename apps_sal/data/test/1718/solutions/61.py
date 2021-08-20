import os
import sys
import numpy as np


def main():
    (N, K) = list(map(int, input().split()))
    A = np.array(list(map(int, input().split())))
    cnt = 0
    i = 0
    while i != N - 1:
        if i == 0:
            A[i:i + K] = np.min(A[i:i + K])
            cnt += 1
            i = i + K - 1
        elif i + K < N:
            A[i:i + K] = A[i]
            cnt += 1
            i = i + K - 1
        else:
            A[i:-1] = A[i]
            cnt += 1
            break
    print(cnt)


def __starting_point():
    main()


__starting_point()
