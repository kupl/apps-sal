class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n

    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]

    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return
        if self.parents[x]>self.parents[y]:
            x,y=y,x
        self.parents[x]+=self.parents[y]
        self.parents[y]=x

    def size(self,x):
        return -self.parents[self.find(x)]

    def same(self,x,y):
        return self.find(x)==self.find(y)
 
    def members(self,x):
        root=self.find(x)
        return [i for i in range(self.n) if self.find(i)==root]
 
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x<0]
 
    def group_count(self):
        return len(self.roots())
 
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
 
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
n=int(input())
X=[]
Y=[]
for i in range(n):
    x,y=map(int,input().split())
    X.append([x,i])
    Y.append([y,i])
X.sort()
Y.sort()
E=[]
for i in range(n-1):
    E.append([X[i+1][0]-X[i][0],X[i][1],X[i+1][1]])
    E.append([Y[i+1][0]-Y[i][0],Y[i][1],Y[i+1][1]])
E.sort()
U=UnionFind(n)
ans=0
for i in range(2*n-2):
    d=E[i][0]
    j1=E[i][1]
    j2=E[i][2]
    if not U.same(j1,j2):
        ans+=d
        U.union(j1,j2)
print(ans)
