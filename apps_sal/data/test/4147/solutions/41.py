n,a,b,c=map(int,input().split())
l=[]
for _ in range(n):
    lt=int(input())
    l.append(lt)
from itertools import product
count=10**10
for i in product([0,1,2,3],repeat=n):
    if i.count(0)>=1 and i.count(2)>=1 and i.count(1)>=1:
    
        temp=0
        at=0
        bt=0
        ct=0
        for j in range(n):
            if i[j]==0:
                at+=l[j]
                temp+=1

            elif i[j]==1:
                bt+=l[j]
                temp+=1
            
            elif i[j]==2:
                ct+=l[j]
                temp+=1
        count=min(count,abs(a-at)+abs(b-bt)+abs(c-ct)+10*(temp-3))
        
print(count)
