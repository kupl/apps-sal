import numba
from numba import jit
import numpy as np


@jit
def main(r, c):
    dp = np.zeros((c + 1, 4), np.int64)
    for i in range(r):
        new_dp = np.zeros((c + 1, 4), np.int64)
        for j in range(4):
            new_dp[:, 0] = np.maximum(new_dp[:, 0], dp[:, j])
        dp = new_dp
        for k in range(c):
            for l in range(2, -1, -1):
                dp[k, l + 1] = max(dp[k, l + 1], dp[k, l] + item_map[i, k])
            for m in range(1, 4):
                dp[k + 1, m] = max(dp[k + 1, m], dp[k, m])
    return max(dp[c - 1, :])


(R, C, K) = list(map(int, input().split()))
item_lis = list((list(map(int, input().split())) for i in range(K)))
item_map = np.zeros((R, C), np.int64)
for (i, j, k) in item_lis:
    item_map[i - 1, j - 1] = k
print(main(R, C))
