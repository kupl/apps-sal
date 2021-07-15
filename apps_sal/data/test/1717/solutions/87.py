
import numpy as np
N=int(input())
x=1
for i in range(2,N+1):
    x=np.lcm(x,i)
print(x+1)
