import numpy as np
(n, k) = list(map(int, input().split()))
A = np.array(sorted(list(map(int, input().split()))), np.int64)
posA = A[A > 0]
negA = A[A < 0]
z = (A == 0).sum()
left = -10 ** 18
right = 10 ** 18
while left + 1 < right:
    num = (left + right) // 2
    count = 0
    if num >= 0:
        count += z * n
    limit_pos = num // posA
    limit_idx = np.searchsorted(A, limit_pos, side='right')
    count += limit_idx.sum()
    limit_neg = -(-num // negA)
    limit_idx = n - np.searchsorted(A, limit_neg, side='left')
    count += limit_idx.sum()
    duplicate_cases = (A ** 2 <= num).sum()
    count -= duplicate_cases
    count //= 2
    if count >= k:
        right = num
    else:
        left = num
print(right)
