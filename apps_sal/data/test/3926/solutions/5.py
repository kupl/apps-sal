from collections import deque
n,m = [int(x) for x in input().split()]
x,y = [int(x) for x in input().split()]
left,right = [int(x) for x in input().split()]
s=[]
ans=0
d=[None]*2007
for i in range(0,2007):
    d[i]=[0 for j in range(0,2007)]

for i in range(0,n):
    s.append(input())

q = deque()

q.append([x-1,y-1,left,right])

while(len(q)):
    v = q[0]
    q.popleft()
    
    if(v[0]<0 or v[0]>=n or v[1]<0 or v[1]>=m or d[v[0]][v[1]]==1 or v[2]<0 or v[3]<0 or s[v[0]][v[1]]=='*'): continue
    
    d[v[0]][v[1]]=1
    
    q.appendleft([v[0]+1,v[1],v[2],v[3]])
    q.appendleft([v[0]-1,v[1],v[2],v[3]])
    q.append([v[0],v[1]+1,v[2],v[3]-1])
    q.append([v[0],v[1]-1,v[2]-1,v[3]])
       
   
    
    
for i in range(0,n):
    for j in range(0,m):
        ans+=d[i][j]

print(ans)

