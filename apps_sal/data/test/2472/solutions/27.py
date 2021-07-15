import numpy as np
N = int(input())
A_list =[0]*N
B_list =[0]*N
for i in range(N):
    A_list[i],B_list[i] = list(map(int,input().split()))
x = np.argsort(B_list)
A_list = np.array(A_list)[x]
B_list = np.array(B_list)[x]
ans = 0
for i,j in zip(A_list,B_list):
    ans +=i
    if(ans<=j):
        pass
    else:
        print('No')
        return
print('Yes')

