import numpy as np
n,m=map(int,input().split())
x=[list(map(int,input().split())) for i in range(m)]
print(max(np.min(x,axis=0)[1]-np.max(x,axis=0)[0]+1,0))
