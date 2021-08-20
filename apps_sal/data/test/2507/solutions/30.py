import numpy as np
(n, k) = list(map(int, input().split()))
A = np.array(input().split(), np.int)
F = np.array(input().split(), np.int)
A.sort()
F.sort()
F = F[::-1]
left = -1
right = (A * F).sum()
while right - left > 1:
    split_line = (left + right) // 2
    r = np.maximum(0, A - split_line // F).sum() <= k
    if r:
        right = split_line
    else:
        left = split_line
print(right)
