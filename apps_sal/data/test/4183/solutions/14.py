import numpy as np
n = int(input())
lis = []
for i in range(n):
    lis.append(int(input()))
print(np.lcm.reduce(lis))
