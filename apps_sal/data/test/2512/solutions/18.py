import numpy as np
from numba import jit


def test():
    R, C, K = list(map(int, input().split()))
    rcv = [list(map(int, input().split())) for _ in range(K)]

    items = np.zeros((R + 1, C + 1), dtype='int64')
    for item in rcv:
        items[item[0]][item[1]] = item[2]

    dp = np.zeros((R + 1, C + 1), dtype='int64')

    # まずは3個の制約がない場合での実装
    for j in range(1, R + 1):
        for i in range(1, C + 1):
            # 下に行く遷移
            dp[j][i] = max(dp[j][i], dp[j - 1][i] + items[j][i])

            # 右に行く遷移
            dp[j][i] = max(dp[j][i], dp[j][i - 1] + items[j][i])

    print((dp[R][C]))


@jit
def main(R, C, items):

    dp = np.zeros((4, R + 1, C + 1), dtype=np.int64)

    # 3個の制約がある場合の実装
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            for k in range(4):
                # 下に行く遷移
                # 取らない場合
                dp[0][i][j] = max(dp[0][i][j], dp[k][i - 1][j])
                # 取る場合
                dp[1][i][j] = max(dp[1][i][j], dp[k][i - 1][j] + items[i][j])

                # 右に行く遷移
                # 取らない場合
                dp[k][i][j] = max(dp[k][i][j], dp[k][i][j - 1])
                # 取る場合
                if k > 0:
                    dp[k][i][j] = max(dp[k][i][j], dp[k - 1]
                                      [i][j - 1] + items[i][j])

    ans = 0
    for k in range(4):
        if ans < dp[k][R][C]:
            ans = dp[k][R][C]

    print(ans)


def __starting_point():
    R, C, K = list(map(int, input().split()))
    rcv = [list(map(int, input().split())) for _ in range(K)]
    items = np.zeros((R + 1, C + 1), dtype=np.int64)
    for item in rcv:
        items[item[0]][item[1]] = item[2]
    main(R, C, items)


__starting_point()
