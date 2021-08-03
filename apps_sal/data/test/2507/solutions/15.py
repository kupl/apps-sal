from sys import stdin
import numpy as np


def main():
    # 入力
    readline = stdin.readline
    n, k = map(int, readline().split())
    A = np.array(list(map(int, readline().split())), dtype=np.int64)
    A = np.sort(A)[::-1]
    F = np.array(list(map(int, readline().split())), dtype=np.int64)
    F = np.sort(F)

    l = -1
    r = 10**12
    while l < r - 1:
        x = (l + r) // 2
        A_after = np.minimum(x // F, A)
        cnt = (A - A_after).sum()
        if cnt <= k:
            r = x
        else:
            l = x

    print(r)


def __starting_point():
    main()


__starting_point()
