import numpy as np
K, X = map(int, input().split())
a = np.arange(X - K + 1, X + K)
print(*a)
