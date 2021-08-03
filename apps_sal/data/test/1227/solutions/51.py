import numpy as np

N = list(map(int, input()))
K = int(input())
l = len(N)
if l < K:
    print((0))
    return

# dp[d][k] := d 桁目まで見て 0 でない数字が k 個ある場合の数
dp_small = np.zeros((l + 1, K + 1), dtype=np.int64)
dp_large = np.zeros((l + 1, K + 1), dtype=np.int64)
dp_large[0, 0] = 1
for d, digit in enumerate(N, 1):
    for k in range(K + 1):
        # 0 を配置する
        dp_small[d, k] += dp_small[d - 1, k]
        if digit != 0:
            dp_small[d, k] += dp_large[d - 1, k]
            dp_large[d, k] = 0
        else:
            dp_large[d, k] = dp_large[d - 1, k]
        if k != 0:
            # 0 以外を配置する
            dp_small[d, k] += dp_small[d - 1, k - 1] * 9
            if digit >= 1:
                dp_small[d, k] += dp_large[d - 1, k - 1] * (digit - 1)
                dp_large[d, k] += dp_large[d - 1, k - 1]
print((dp_small[l, K] + dp_large[l, K]))
