n=int(input())
A=[]
for i in range(n):
    A.append(int(input()))

import numpy as np
print(np.lcm.reduce(A))
