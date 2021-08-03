import numpy as np

N = int(input())
S = np.array([int(x) for x in input().split()], dtype=np.int64)

# 右移動着地点：等差数列、ゴール含む
# 左移動着地点：等差数列、スタート含む

answer = 0
for d in range(1, N):
    # d = A-B
    cum_left = np.cumsum(S[::d])
    cum_right = np.cumsum(S[::-1][::d])
    score = cum_left + cum_right  # 等差数列の長さ-1 -> 得点
    # あとは、その経路がルール内で実現できるかどうか
    for L, s in enumerate(score):
        if answer >= s:
            continue
        # 右左に進んでいることの確認
        A = N - 1 - L * d
        B = A - d
        if A <= 0:
            continue
        if A <= B:
            continue
        if B <= 0:
            continue
        # 同じ場所を取っていないかの確認
        # kd = N-1-ldとなるとまずい
        # 約数のとき、Ld >= N-Ldだとまずい
        if (N - 1) % d == 0 and 2 * L * d >= N - 1:
            continue
        answer = s

print(answer)
