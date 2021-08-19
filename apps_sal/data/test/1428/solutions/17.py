from sys import stdin
import numpy as np


def main():
    # 入力
    readline = stdin.readline
    n, max_c = map(int, readline().split())
    d = [list(map(int, readline().split())) for _ in range(max_c)]
    d = np.array(d, dtype=np.int64)
    c = [list(map(lambda x:int(x) - 1, readline().split())) for _ in range(n)]

    # 前処理
    color_table = np.zeros((3, max_c), dtype=np.int64)
    for i in range(n):
        for j in range(n):
            color_table[(i + j + 2) % 3, :] += d[c[i][j], :]

    # 全探索
    ans = float("inf")
    for i in range(max_c):
        for j in range(max_c):
            for k in range(max_c):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, color_table[0][i] + color_table[1][j] + color_table[2][k])

    print(ans)


def __starting_point():
    main()


__starting_point()
