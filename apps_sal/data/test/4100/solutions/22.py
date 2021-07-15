import numpy as np
n,k,q = map(int,input().split())
a =np.array([k-q]*n)
for i in range(q):
    a[int(input())-1]+=1
for i in a:
    if i>0:
        print("Yes")
    else:
        print("No")
