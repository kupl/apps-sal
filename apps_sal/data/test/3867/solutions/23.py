import sys
from collections import deque
n=int(input())
visited=[False for i in range(n+1)]
dp=[0 for i in range(n+1)]
l=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=list(map(int,input().split()))
    l[a].append(b)
    l[b].append(a)
b=list(map(int,input().split()))
s=[1]
visited[1]=True
c=1
c1=0
t=True
while len(s)!=n :
    aux=0
    for i in l[s[c1]]:
        if not visited[i]:
            visited[i]=True
            dp[i]=1
            aux+=1
    for i in range(c,c+aux):
        if dp[b[i]]==1:
            s.append(b[i])
            dp[b[i]]=0
        else:
            print("No")
            t=False
            break
    else:
        c+=aux
        c1+=1
        continue
    break
if t:
    print("Yes")

