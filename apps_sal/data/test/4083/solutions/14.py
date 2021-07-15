from collections import defaultdict as DD
import sys
MOD=pow(10,9)+7

def IN(f=0):
    if f==0:
        return ( [int(i) for i in sys.stdin.readline().split()] )
    else:
        return ( int(sys.stdin.readline()) )

n,k=IN()
a=IN()
b=[]

d=DD(list)
for x in a:
    i=0
    while(x!=0):
        d[x].append(i)
        x=x//2
        i+=1
    d[0].append(i)
    #print(d)

ans=9999999999999
for x in d:
    if len(d[x])>=k:
        r=d[x]
        r.sort()
        ans=min(ans,sum(r[:k]))
print(ans)
        



