import numpy as np
n = input()
print(*np.argsort(list(map(int, input().split()))) + 1)
