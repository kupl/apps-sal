f=lambda : map(int,input().split())
N=input()
*A,=f()
import collections
c = collections.Counter(A)
s=sum(A)
BC=[f() for _ in range(int(input()))]

for i,j in BC:
 v=c[i]
 s+=v*(j-i)
 print(s)
 c[j]+=v
 c[i]=0
