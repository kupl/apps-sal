import numpy as np
N, D = map(int, input().split())

print(int(np.ceil(N / (2 * D + 1))))
