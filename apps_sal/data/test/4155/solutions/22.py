n=int(input())
*h,=map(int, input().split())
import numpy as np
h=np.array(h)

def rec(hh):
    if len(hh)==0:
        return 0
    if len(hh)==1:
        return hh[0]
    i=np.argmin(hh)
    res=hh[i]
    l=rec(hh[:i]-hh[i])
    r=rec(hh[i+1:]-hh[i])
    return res+l+r
print(rec(h))
