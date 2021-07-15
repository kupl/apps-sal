import sys
input=lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(200000)
mod=10**9+7
n=int(input())
edge=[[] for i in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  edge[a-1].append(b-1)
  edge[b-1].append(a-1)
inf=10**6
Par=[inf]*n
Par[0]=-1
Chk=[0]
while Chk:
  c=Chk.pop()
  for next in edge[c]:
    if Par[next]==inf:
      Par[next]=c
      Chk.append(next)

C=[-1]*n
def ch(x):
  ret=0
  if x!=0 and len(edge[x])==1:
    C[x]=0
    return C[x]
  else:
    for e in edge[x]:
      if e==Par[x]:
        continue
      else:
        ret+=ch(e)+1
    C[x]=ret
    return C[x]
ch(0)

H=[0]*n
H[0]=1
H[1]=pow(2,mod-2,mod)
for i in range(2,n):
  H[i]=(H[i-1]*H[1])%mod

ans=0
for i in range(n):
  if len(edge[i])==1:
    continue
  else:
    A=[]
    for e in edge[i]:
      if e==Par[i]:
        A.append(n-1-C[i])
      else:
        A.append(C[e]+1)
    cur=1+(len(edge[i])-1)*H[-1]
    for a in A:
      cur-=H[n-1-a]
    ans=(ans+cur)%mod
print((ans*H[1])%mod)
