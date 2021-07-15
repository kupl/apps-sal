import numpy as np
n,k = list(map(int,input().split()))

a = np.array([0]*n,dtype ='int64')
a[0] += n
for i in range(1,n):
    c = n // (1+i)
    d = n % (1+i)
    a[1:i+1] += c
    a[0] +=c
    if d > 0:
        a[1:d+1] +=1
print((np.sum(a[k:])))

