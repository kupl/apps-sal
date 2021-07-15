import numpy as np

x = np.array(list(map(int, input().split())))
y = np.arange(1,6)
print(-sum(x-y))
