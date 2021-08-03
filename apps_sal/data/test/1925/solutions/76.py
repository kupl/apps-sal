import numpy as np
A, B, N = map(int, input().split())
if B <= N:
    x = B - 1
    print(int(np.floor(A * x / B)))
else:
    print(int(np.floor(A * N / B)))
