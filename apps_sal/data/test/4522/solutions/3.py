import sys
input = sys.stdin.readline
n,m=list(map(int,input().split()))
par=[-1]*n
def c(x):
  return x*(x-1)//2

def find(x):
  if par[x]<0:
    return x
  else:
    par[x]=find(par[x])
    return par[x]

def unite(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return False
  else:
    if par[x]>par[y]:
      x,y=y,x
    par[x]+=par[y]
    par[y]=x
    return True

def same(x,y):
  return find(x)==find(y)

def size(x):
  return -par[find(x)]
import collections
Edge=collections.defaultdict(list)
for _ in range(n-1):
  u,v,w=list(map(int,input().split()))
  Edge[w].append((u,v))
Q=[int(i) for i in input().split()]
q=max(Q)
Ans=[0]*(q+1)
ans=0
for i in range(1,q+1):
  for u,v in Edge[i]:
    if same(u-1,v-1):
      continue
    else:
      uu,vv=size(u-1),size(v-1)
      unite(u-1,v-1)
      uv=size(u-1)
      ans+=c(uv)-c(uu)-c(vv)
  Ans[i]=ans
Ans2=[]
for q in Q:
  Ans2.append(Ans[q])
print(*Ans2)


