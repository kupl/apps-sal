class UnionFind():
  def __init__(self,n):
    self.parents=[-1]*n
  
  def find(self,x):
    if self.parents[x]<0:
      return x
    self.parents[x]=self.find(self.parents[x])
    return self.parents[x]
  
  def union(self,x,y):
    x = self.find(x)
    y = self.find(y)
    if x==y:
      return
    
    if self.parents[x]>self.parents[y]:
      x,y=y,x
    
    self.parents[x]+=self.parents[y]
    self.parents[y]=x

N,M=map(int,input().split())
ans=0
A=[]
B=[]

for _ in range(M):
  a,b=map(int,input().split())
  A.append(a)
  B.append(b)
  
for i in range(M):
  uf=UnionFind(N+1)
  for j in range(M):
    if i==j:
      continue
    uf.union(A[j],B[j])
  else:
    if abs(min(uf.parents[1:]))!=N:
      ans+=1
print(ans)
