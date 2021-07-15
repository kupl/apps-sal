n,m=list(map(int,input().split()))
ab=[[] for _ in range(10**5+1)]
for j in range(1,10**5+1):
    ab[j].append(0)

for _ in range(n):
    a,b=list(map(int,input().split()))
    ab[a].append(-1*b)


temp=[]
import heapq
ans=0
for i in range(1,m+1):
    for j in ab[i]:
        heapq.heappush(temp,j)
    
    x=heapq.heappop(temp)
    
    ans+=-1*x
print(ans) 

