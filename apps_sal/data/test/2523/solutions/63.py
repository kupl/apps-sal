# [a,b] - [a,b) = {b} なので、端の方は自由。
# 中央が単色であるかを確認すればよい。

import numpy as np
arr = np.array([int(x) for x in input()])
arr_c = arr.cumsum()

N = arr.size

answer = 0

for K in range(N, 0, -1):
    left = N - K
    right = K - 1
    # [left,right]が単色であればよい
    if left >= right:
        answer = K
        break
    one_cnt = arr_c[right] - arr_c[left] + arr[left]
    zero_cnt = (right - left + 1) - one_cnt
    if one_cnt == 0 or zero_cnt == 0:
        answer = K
        break

print(answer)
