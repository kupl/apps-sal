import numpy as np
n=int(input())
a=np.array(list(map(int,input().split())))
d=np.array([0]*(10**5+2))
for i in a:
    for j in (-1,0,1):
        d[i+1+j]+=1
print(max(d))
