# cook your dish here
from collections import defaultdict
pr = defaultdict(int)
N=2750132
d=[0]*N
k=1
for i in range(2,N):
    if d[i]==0:
        pr[i]=k
        k=k+1
        d[i]=1
        for j in range(i*i,N,i):
            if d[j]==0:
                d[j]=j//i
        
n=int(input())
b=list(map(int,input().split()))

c=[0]*N
for j in b:
    c[j]+=1

a=[]
for i in range(N-1,2,-1):
    if c[i]>0:
        for k in range(c[i]):
            if d[i]==1:
                t=pr[i]
                a.append(t)
                c[t]-=1
            else:
                a.append(i)
                #print(d[i],c[i],i)
                c[d[i]]-=1
    
print(*a)
            
        
        
        
        

