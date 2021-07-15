3
from collections import deque
def dfs ():
  while(len(queue)!=0):
    s=queue.popleft()
    (i,j)=s
    for (ni,nj) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:      
      if ni in range(0,n) and nj in range(0,m):
        fl=data[ni][nj]
        if(e == (ni,nj)) and fl=="X":
          return True
        elif fl == ".":
          data[ni][nj] = "X"
          queue.append((ni,nj))
  return False
[n,m]=list(map(int,(input().split())))
data=list()
for i in range(0,n):
  data.append(list([x for x in input()]))
[si,sj]=list(map(int,(input().split())))
[ei,ej]=list(map(int,(input().split())))
e=(ei-1,ej-1)
queue=deque()
queue.append((si-1,sj-1))
print("YES" if dfs() else "NO")  

