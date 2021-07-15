from collections import deque
n=int(input())
visited=[False for i in range(n+2)]
dp=[-1 for i in range(n+2)]
l=[[] for i in range(n+2)]
for i in range(n-1):
    a,b=list(map(int,input().split()))
    l[a].append(b)
    l[b].append(a)
b=deque(list(map(int,input().split())))
b.popleft()
s=deque([1])
ans="Yes"
visited[1]=True
while len(b)>0 and len(s)>0:
    aux=0
    for i in l[s[0]]:
        if not visited[i]:
            visited[i]=True
            dp[i]=1
            aux+=1
    for i in range(aux):
        x=b.popleft()
        if dp[x]==1:
            s.append(x)
            dp[x]=-1
        else:
            ans="No"
            b=[]
            break
    s.popleft()
print(ans)
            
            
    
            

