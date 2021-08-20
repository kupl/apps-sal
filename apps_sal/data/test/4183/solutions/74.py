import numpy as np
n = int(input())
A = []
for i in range(n):
    A.append(int(input()))
print(np.lcm.reduce(A))
