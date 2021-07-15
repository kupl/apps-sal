import numpy as np

w,h,n = map(int,input().split())
b = np.zeros((h,w),dtype=np.int)

for i in range(n):
    x,y,a = map(int,input().split())
    if a == 1:
        b[:,:x] = 1
    elif a == 2:
        b[:,x:] = 1
    elif a == 3:
        b[:y,:] = 1
    else:
        b[y:,:] = 1
print(np.count_nonzero(b < 1))
