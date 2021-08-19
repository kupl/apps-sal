import numpy as np
N = int(input())
a = list(map(int, input().split()))
a = np.array(a)
cum = np.cumsum(a)[:-1]
rcum = np.cumsum(a[::-1])[:-1]
ans = abs(cum - rcum[::-1])
print(np.min(ans))
