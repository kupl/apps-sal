#abc129d
import numpy as np
h,w=list(map(int,input().split()))
s=np.array([list(input()) for i in range(h)])=='.'
u=np.zeros((h,w),dtype=int)
d=np.zeros((h,w),dtype=int)
l=np.zeros((h,w),dtype=int)
r=np.zeros((h,w),dtype=int)
for i in range(h):
 u[i]=(u[i-1]+1)*s[i]
 d[-i-1]=(d[-i]+1)*s[-i-1]
for i in range(w):
 l[:,i]=(l[:,i-1]+1)*s[:,i]
 r[:,-i-1]=(r[:,-i]+1)*s[:,-i-1]
print((np.max(u+d+l+r-3)))

