import math
import numpy as np
n = int(input())
X = np.array(list(map(int, input().split())))
lower = min(X)
upper = max(X)
ans = (X - lower) ** 2
ans = ans.sum()
for i in range(lower + 1, upper + 1):
    m = (X - i) ** 2
    if m.sum() < ans:
        ans = m.sum()
print(ans)
