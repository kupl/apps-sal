import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))
ans = np.argsort(a)
print(*ans + 1)
