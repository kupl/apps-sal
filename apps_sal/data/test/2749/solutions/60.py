from collections import deque
h,w=list(map(int,input().split()))
n=int(input())
a=list(map(int,input().split()))
ae=[]
ans=[]
rl=0
for i in range(n):
  ae.extend([i+1]*a[i])
for x in range(h):
  if x%2==0:
    ans.append(ae[w*x:w*(x+1)])
  else:
    ans.append(reversed(ae[w*x:w*(x+1)]))

for r in ans:
  print((' '.join(list(map(str,r)))))
  
  
  

