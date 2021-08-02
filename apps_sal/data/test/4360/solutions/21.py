import numpy as np
N, *A = map(int, open(0).read().split())
print(1 / np.sum(1 / np.array(A)))
