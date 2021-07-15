import numpy as np
X = np.array([int(x) for x in input().split()])
ans = np.ceil(np.mean(X))
print(int(ans))
