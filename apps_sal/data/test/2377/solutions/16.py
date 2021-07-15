
from bisect import bisect_left,bisect
import sys

n,h=list(map(int,input().split()))
#ab=[[0]*2 for i in range(n)]
a=[0]*n
b=[0]*n
for i in range(n):
#    ab[i]=map(int,input().split())
    a[i],b[i]=list(map(int,input().split()))
 
amax=max(a)    
b.sort()
ii=bisect(b,amax)
b=b[ii:]
b.reverse()

icnt=0
for bi in b:
    icnt+=1
    h=h-bi
    if h<=0:
        print(icnt)
        return

di=(h-1)//amax+1
print((icnt+di))

