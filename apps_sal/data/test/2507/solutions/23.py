import numpy as np
(N, K) = map(int, input().split())
A = np.array(list(map(int, input().split())))
F = np.array(list(map(int, input().split())))
A.sort()
F.sort()
A = A[::-1]
left = 0
right = np.max(A * F)
for _ in range(50):
    judge = (left + right) // 2
    rec = judge // F
    recK = np.sum(np.maximum(np.zeros(N), A - rec))
    if recK <= K:
        right = judge
    else:
        left = judge + 1
    if left == right:
        print(left)
        break
