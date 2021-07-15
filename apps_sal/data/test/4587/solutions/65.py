import numpy as np
N = int(input())
A = np.array(input().split(), dtype=np.int32)
B = np.array(input().split(), dtype=np.int32)
C = - np.array(input().split(), dtype=np.int32)
 
A.sort()
B.sort()
C.sort()
 
cnt_A = np.searchsorted(A,B,side='left')
cnt_C = np.searchsorted(C,-B,side='left')
 
answer = (cnt_A * cnt_C).sum()
print(answer)
