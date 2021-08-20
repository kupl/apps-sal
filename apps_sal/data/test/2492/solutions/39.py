import numpy as np
(n, k) = list(map(int, input().split()))
A = np.array(input().split(), np.int64)
A.sort()
posA = A[A > 0]
negA = A[A < 0]
zeros = (A == 0).sum()
left = -10 ** 18
right = 10 ** 18
while left + 1 < right:
    num = (left + right) // 2
    less_count = 0
    if num >= 0:
        less_count += zeros * n
    limit_pair_for_pos = num // posA
    limit_idxs = np.searchsorted(A, limit_pair_for_pos, side='right')
    less_count += limit_idxs.sum()
    limit_pair_for_neg = -(num // -negA)
    limit_idxs = n - np.searchsorted(A, limit_pair_for_neg, side='left')
    less_count += limit_idxs.sum()
    duplicate_cases = (A ** 2 <= num).sum()
    less_count -= duplicate_cases
    less_count //= 2
    if less_count >= k:
        right = num
    else:
        left = num
print(right)
