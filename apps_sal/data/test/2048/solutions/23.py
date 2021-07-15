from heapq import heappush
import bisect
n=int(input())
s=list(map(int,input().split()))
c=list(map(int,input().split()))
a={}
b=[]
ak=[]
aki=[]
for i in range(n-1,-1,-1):
    ind0=bisect.bisect(ak,s[i])
    ak.insert(ind0,s[i])
    aki.insert(ind0,i)
    a[i]=[]
    ind=-1
    for j in aki[ind0:]:
        if s[j]>s[i]:
            if len(a[j])==1:
                heappush(b,c[i]+c[j]+c[a[j][0]])
            if ind==-1 or m>=c[j]:
                m,ind=c[j],j
    if ind!=-1:
        a[i]=[ind]
if b:
    print(b[0])
else:
    print(-1)
