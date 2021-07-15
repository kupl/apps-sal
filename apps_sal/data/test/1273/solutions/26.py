f=lambda:map(int,input().split())
n=int(input())
g=[[] for _ in range(n)]
for i in range(n-1):
  a,b=f()
  g[a-1]+=[(b-1,i)]
  g[b-1]+=[(a-1,i)]
l=[0]*(n-1)
u=[0]*n
q=[(0,0)]
while q:
  v,s=q.pop()
  u[v]=1
  t=1
  for c,i in g[v]:
    if u[c]: continue
    if t==s: t+=1
    l[i]=t
    q+=[(c,t)]
    t+=1
print(max(l))
for i in l: print(i)
