import sys 
from collections import deque
N = int(input())
A = list(map(int, input().split()))


if N == 1:
    print((A[0]))
    return

mae = deque()
usiro = deque()

#0の時に前 1の時に後ろ
Flag = 0

for i in reversed(list(range(0,N,1))):
    
    if Flag == 0: # 前の時
        mae.append(str(A[i]))
        mae.append(" ")
        Flag = 1
    else:
        usiro.insert(0,str(A[i]))
        usiro.appendleft(" ")
        Flag = 0

moziretu = (mae + usiro)
del moziretu[((len(moziretu))//2)]
moziretu = ''.join(moziretu)
print(moziretu)
  
  



