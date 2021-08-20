import numpy as np
(A, B, C, D) = map(int, input().split())
a = [0 for _ in range(100)]
b = [0 for _ in range(100)]
a[A:B] = [1 for _ in range(B - A)]
b[C:D] = [1 for _ in range(D - C)]
c = np.array(a) * np.array(b)
print(c.sum())
