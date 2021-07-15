import numpy as np
import bisect
N,M,K= list(map(int, input().split()))
A=list(map(int, input().split()))
B=list(map(int, input().split()))
if A[0]>K and B[0]>K:print((0));return

Asum=[0]
for i in range(N):
  if Asum[-1]+A[i]<=K:
    Asum.append(Asum[-1]+A[i])  
  else:break
    
Bsum=[0]
for j in range(M):
  if Bsum[-1]+B[j]<=K:
    Bsum.append(Bsum[-1]+B[j])
  else:break
    #AAsum=[]
#for i in range(len(Asum)):
#  AAsum.append(K-Asum[i])

#print(Asum)
#print(AAsum)
#print(Bsum)

C=[]
for i in range(len(Asum)):
  C.append(bisect.bisect(Bsum,K-Asum[i])+i-1)

#print(Asum)
#print(AAsum)
#print(Bsum)
#print(C)
print((max(C)))
#176882

