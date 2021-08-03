import numpy as np
N = int(input())
X = list(map(int, input().split()))
p = np.floor(np.mean(X))
ans = min(np.sum([(x - p)**2 for x in X]), np.sum([(x - (p + 1))**2 for x in X]))

print(int(ans))
