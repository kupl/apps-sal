

import os
import sys


def main():
    N, M = list(map(int, input().split()))
    path = []
    for _ in range(N):
        A, B = list(map(int, input().split()))
        path.append([A, B])
    path.sort(key=lambda x: x[0])
    ans = [0, 0]
    for p in path:
        if ans[1] + p[1] <= M:
            ans[0] = ans[0] + p[0] * p[1]
            ans[1] += p[1]

        else:
            num = M - ans[1]
            ans[0] = ans[0] + p[0] * num
            ans[1] = ans[1] + num
        if ans[1] == M:
            print((ans[0]))
            return


def __starting_point():
    main()


__starting_point()
