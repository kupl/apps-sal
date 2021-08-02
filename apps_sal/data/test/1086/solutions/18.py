import numpy as np
H, W = map(int, input().split())
red_map = np.array([input().split() for i in range(H)], dtype="int")
blue_map = np.array([input().split() for i in range(H)], dtype="int")
sub_map = abs(red_map - blue_map)
dp = [[2020] * W for i in range(H)]
max_deviation = 2**(80 * (H + W))

for i in range(H):
    for j in range(W):
        if not i and not j:
            dp[i][j] = (max_deviation << sub_map[i][j] | max_deviation >> sub_map[i][j])
        if i > 0:
            dp[i][j] |= (dp[i - 1][j] << sub_map[i][j] | dp[i - 1][j] >> sub_map[i][j])
        if j > 0:
            dp[i][j] |= (dp[i][j - 1] << sub_map[i][j] | dp[i][j - 1] >> sub_map[i][j])

pre_ans = dp[H - 1][W - 1] >> 80 * (H + W)
pre_ans_bit = format(pre_ans & -pre_ans, "b")
ans = len(pre_ans_bit) - 1
print(ans)
