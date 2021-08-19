from sys import stdin
import numpy as np


def main():
    # 入力
    readline = stdin.readline
    n, m, q = map(int, readline().split())
    table = np.array([[0] * n for _ in range(n)], dtype="int64")
    for i in range(m):
        l, r = map(lambda x: int(x) - 1, readline().split())
        table[l][r] += 1

    # 累積和
    for i in range(n):
        table[i] = table[i].cumsum()

    ans = [0] * q
    for i in range(q):
        l, r = map(lambda x: int(x) - 1, readline().split())
        ans[i] = table[l:r + 1, r].sum()

    for i in range(q):
        print(ans[i])


def __starting_point():
    main()


__starting_point()
