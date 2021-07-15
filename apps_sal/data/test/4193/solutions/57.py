import numpy as np

A1=np.array(list(map(int,input().split())))
A2=np.array(list(map(int,input().split())))
A3=np.array(list(map(int,input().split())))
A=np.concatenate([A1,A2,A3]).reshape(3,3)

N=int(input())

for i in range(N):
    b=int(input())
    A[np.where(A==b)] = 0

if np.all(A[0,:]==0) or np.all(A[1,:]==0) or np.all(A[2,:]==0) or np.all(A[:,0]==0) or np.all(A[:,1]==0) \
    or np.all(A[:,2]==0) or A[0,0]**2+A[1,1]**2+A[2,2]**2==0 or A[0,2]**2+A[1,1]**2+A[2,0]**2==0:
    print('Yes')
else:
    print('No')
