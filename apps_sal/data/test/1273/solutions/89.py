N=int(input())
l=[[] for i in range(N)]
color=[0]*N
mem=[]
for i in range(N-1):
   a,b=list(map(int,input().split()))
   a-=1;b-=1
   l[a].append(b)
   mem.append(b)
from collections import deque
que=deque([0])
while que:
   node=que.popleft()
   c=1
   for i in l[node]:
      if color[node]==c:
         c+=1
      color[i]=c
      c+=1
      que.append(i)
print(max(color))
for i in mem:
   print(color[i])
