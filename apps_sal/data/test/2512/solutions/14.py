import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8
import sys

R, C, K = map(int, input().split())
rcvs = [list(map(int, input().split())) for _ in range(K)]
rcvs = np.array(rcvs, dtype=np.int64)


@njit
def main(rcvs):
    rewards = np.zeros((R, C), dtype=np.int64)

    for i in range(len(rcvs)):
        rewards[rcvs[i][0] - 1][rcvs[i][1] - 1] = rcvs[i][2]

    dp = np.zeros((R + 1, C + 1, 4), dtype=np.int64)

    for i in range(R):
        for j in range(C):
            reward = rewards[i][j]
            dp[i + 1][j + 1][0] = max(dp[i][j + 1])
            dp[i + 1][j + 1][1] = dp[i + 1][j + 1][0] + reward

            for k in range(4):
                dp[i + 1][j + 1][k] = max(dp[i + 1][j][k], dp[i + 1][j + 1][k])
            if reward > 0:
                for k in range(3):
                    dp[i + 1][j + 1][k + 1] = max(dp[i + 1][j][k] + reward, dp[i + 1][j + 1][k + 1])
    return max(dp[-1][-1])


print(main(rcvs))

"""
メモ
ndarrayの型宣言でtype指定できない
typeコマンドも機能しない
iteration使えない
グローバル変数使える
main(As)
"""
