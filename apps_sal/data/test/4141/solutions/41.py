import numpy as np

N=int(input())
A=np.array(list(map(int,input().split())))

A = A[A%2==0]
if (np.all((A%3==0) | (A%5==0))==True):
    print('APPROVED')
else:
    print('DENIED')
