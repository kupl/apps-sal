class Union_Find:
  def __init__(self,n=0):
    self.vertices=n
    self.mother=[-1 for i in range(self.vertices)]
    self.size_temp=[1 for i in range(self.vertices)]
  
  def root(self,x):
    normalize_v=[]
    while x!=-1:
      normalize_v.append(x)
      y=x
      x=self.mother[x]
    for i in normalize_v[:-1]:
      self.mother[i]=y
    return y
  
  def union(self,x,y):
    root_x=self.root(x)
    root_y=self.root(y)
    if root_x!=root_y:
      self.mother[root_x]=root_y
      self.size_temp[root_y]+=self.size_temp[root_x]
  
  def find(self,x,y):
    if self.root(x)==self.root(y):
      return True
    else:
      return False
  
  def size(self,x):
    return self.size_temp[self.root(x)]



n,m,k=list(map(int,input().split()))
uf=Union_Find(n)
friend=[0 for i in range(n)]
block=[[] for i in range(n)]

for i in range(m):
  a,b=[int(x)-1 for x in input().split()]
  friend[a]+=1
  friend[b]+=1
  uf.union(a,b)

for i in range(k):
  a,b=[int(x)-1 for x in input().split()]
  block[a].append(b)
  block[b].append(a)

r=""
for i in range(n):
  size=uf.size(i)
  size-=friend[i]
  for j in block[i]:
    if uf.find(i,j):
      size-=1
  r+=str(size-1)+" "
print((r[:-1]))

