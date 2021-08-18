import numpy as np
n = int(input())
x = 1
for i in range(2, n + 1):
    x = np.lcm(x, i)
print(x + 1)
