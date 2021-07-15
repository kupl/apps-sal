import sys
from collections import defaultdict
n,m,k=list(map(int,sys.stdin.readline().split()))
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))
consa=defaultdict(int)
consb=defaultdict(int)
count=0
arra=set()
arrb=set()
for i in range(n):
    if a[i]==1:
        count+=1
        arra.add(count)
        consa[count]+=1
    else:
        count=0
count=0
for i in range(m):
    if b[i]==1:
        count+=1
        arrb.add(count)
        consb[count]+=1
    else:
        count=0
arra=list(arra)
arrb=list(arrb)
arra.sort()
arrb.sort()
arra.reverse()
arrb.reverse()
prev=0
for i in arra:
    consa[i]+=prev
    prev=consa[i]
prev=0
for i in arrb:
    consb[i]+=prev
    prev=consb[i]
#print(consa,'consa')
#print(consb,'consb')
ans=0
vis=defaultdict(int)
for i in range(1,n+1):
    if k%i==0:
        ans+=consa[i]*consb[k//i]
        vis[k//i]+=1
for i in range(1,m+1):
    if k%i==0 and vis[i]==0:
        ans+=consb[i]*consa[k//i]
print(ans)

