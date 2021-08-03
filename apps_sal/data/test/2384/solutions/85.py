import numpy as np
import itertools

N = int(input())
A = list(map(int, input().split()))

if N % 2 == 0:
    left = np.cumsum([0] + A[::2])
    right = np.cumsum([0] + A[::-2])[::-1]
    ans = max(left + right)
else:
    left = np.cumsum([0] + A[:-1:2])
    mid_left = np.cumsum([0] + A[-2::-2])[::-1]
    mid_right = np.cumsum([0] + A[1::2])
    right = np.cumsum([0] + A[:1:-2])[::-1]

    left_sum = left + mid_left
    left_max = np.zeros(N // 2 + 1, dtype=int)
    left_max[0] = left_sum[0]
    for i in range(1, N // 2 + 1):
        left_max[i] = max(left_max[i - 1], left_sum[i])
    left_max -= mid_left

    right_sum = right + mid_right
    right_max = np.zeros(N // 2 + 1, dtype=int)
    right_max[-1] = right_sum[-1]
    for i in range(N // 2 - 1, -1, -1):
        right_max[i] = max(right_max[i + 1], right_sum[i])
    right_max -= mid_right

    ans = max(left_max + right_max)


print(ans)
