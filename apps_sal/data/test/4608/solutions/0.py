

import os
import sys


def main():
    N = int(input())
    A = [0]
    visited = [0] * (N + 1)
    for _ in range(N):
        A.append(int(input()))
    i = 1
    cnt = 0
    while visited[i] == 0:
        if i == 2:
            print(cnt)
            return
        cnt += 1
        visited[i] = 1
        i = A[i]
    print((-1))


def __starting_point():
    main()


__starting_point()
