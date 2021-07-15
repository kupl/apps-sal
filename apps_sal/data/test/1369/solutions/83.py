from scipy import optimize
import numpy as np

n=int(input())
points=[tuple(map(int,input().split())) for i in range(n)]

maxd=0
def d(xy):
    maxd=0
    x,y=xy
    for p in points:
        px,py=p
        d=np.linalg.norm((x-px,y-py))
        if maxd<d:
            maxd=d
    return maxd
opt=optimize.fmin(d,np.zeros(2),ftol=10**(-6),disp=0)
print(d(opt))
