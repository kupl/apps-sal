from collections import deque

n=int(input())
r=[[] for _ in range(n)]
kumi=[]
for _ in range(n-1):
  s=list(map(int,input().split()))
  kumi.append(str(s[0]-1)+'+'+str(s[1]-1))
  r[s[0]-1].append(s[1]-1)
  r[s[1]-1].append(s[0]-1)
  
  
ans=0
for i in range(n):
  ans=max(len(r[i]),ans)

print(ans)

ans_iro=[[] for _ in range(n)]

iro=[-1 for _ in range(n)]
iro[0]=1
ch=1
d=[]
di={}
for i in r[0]:
  iro[i]=ch
  di[str(min(0,i))+'+'+str(max(0,i))]=ch
  ch+=1
  d.append(i)
  
  

d=deque(d)



while d:
  v=d.popleft()
  ch=1
  for i in r[v]:
    if iro[i]==-1:
      if ch==iro[v]:
        ch+=1
        iro[i]=ch
        di[str(min(v,i))+'+'+str(max(v,i))]=ch
        ch+=1
      else:
        iro[i]=ch
        di[str(min(v,i))+'+'+str(max(v,i))]=ch
        ch+=1
        
      d.append(i)
      
for g in kumi:
  print((di[g]))
      

  



