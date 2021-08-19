# D - Pairs

import numpy as np

N, K = map(int, input().split())
A = np.array(sorted(list(map(int, input().split()))), np.int64)

n_zero = len(A[A == 0])
A_posi = A[A > 0]
A_nega = A[A < 0]


def n_pairs_less_than_or_equal_to_border(product_border):
    n_pairs = -np.sum(A * A <= product_border)  # i==jかつ条件を満たすペアの個数を先に引き、以降重複を許して数える
    n_pairs += n_zero * N * (product_border >= 0)

    n_pairs += np.searchsorted(A, product_border // A_posi, side="right").sum()
    n_pairs += (N - np.searchsorted(A, -(-product_border // A_nega), side="left")).sum()

    # 上記2行は下記と同様の処理だが下記の実装だとTLE
    # for i in range(N):
    #     if A[i] > 0:
    #         n_pairs += np.searchsorted(A, product_border//A[i], side="right")
    #     elif A[i] < 0:
    #         n_pairs += N - np.searchsorted(A, -(-product_border//A[i]), side="left")

    n_pairs //= 2
    return n_pairs


lower = -(10**18)
upper = 10**18

while lower <= upper:
    x = (lower + upper) // 2
    if n_pairs_less_than_or_equal_to_border(x) >= K:
        ans = x
        upper = x - 1
    else:
        lower = x + 1

print(ans)
