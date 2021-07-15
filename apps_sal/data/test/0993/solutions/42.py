N,M=map(int, input().split())
A=list(map(int, input().split()))
import numpy
D=list(numpy.cumsum(A))
C={}
for i in D:
  d=i%M
  if d not in C:
    C[d]=1
  else:
    C[d]+=1
#print(C)

ans=0
for i in C.values():
  ans+=i*(i-1)//2
#余り0はそれ単独でok
if 0 in C:
  ans+=C[0]
print(ans)
