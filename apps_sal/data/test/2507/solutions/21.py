N,K = map(int,input().split())

import numpy as np

A = np.array(input().split(),np.int64)
B = np.array(input().split(),np.int64)

A.sort() ; B.sort() 
B=B[::-1]

right = max(A*B)   #時間の可能集合の端点
left = -1           #時間の不可能集合の端点

def test(t):
    
    C = A-t//B
    D= np.where(C<0,0,C)
    return D.sum()<=K

while left+1<right:
    mid = (left+right)//2
    if test(mid):
        right=mid
    else:
        left = mid

print(right)
