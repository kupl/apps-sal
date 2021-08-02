import numpy as np
n = int(input())
x = np.lcm.reduce(list(range(2, n + 1)), dtype=np.int64) + 1
print(x)
