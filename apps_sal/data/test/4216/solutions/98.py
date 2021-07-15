import math
N=int(input())
sqN=math.floor(math.sqrt(N))
for i in range(sqN):
  if N%(i+1)==0:
    B=N//(i+1)
    B=str(B)
    B=list(map(str,B))
    F=len(B)
print(F)
