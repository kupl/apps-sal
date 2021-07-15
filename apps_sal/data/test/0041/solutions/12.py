from math import *
length=int(input())
a=list(map(int,input().strip().split()))
p=[-inf]
for i in range(length):
    if a[i]==0:
        p.append(i)
p.append(inf)
i=0
j=1
b=[0 for _ in range(length)]
for k in range(length):
    if k<p[j]:
        b[k]=min(k-p[i],p[j]-k)
    if k==p[j]:
        j+=1
        i+=1
for i in b:
    print(i,end=' ')

