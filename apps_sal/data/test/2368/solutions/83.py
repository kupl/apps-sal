N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
CD=[list(map(int,input().split())) for i in range(M)]
class UnionFind:
    def __init__(self,N):
        self.Parent=[-1]*N
    def unite(self,m,n):
        rm=self.root(m)
        rn=self.root(n)
        if rm==rn:
            return False
        else:
            if self.size(rm)<self.size(rn):
                rm,rn=rn,rm
            self.Parent[rm]+=self.Parent[rn]
            self.Parent[rn]=rm
            return True
    def root(self,n):
        if self.Parent[n]<0:
            return n
        else:
            self.Parent[n]=self.root(self.Parent[n])
            return self.Parent[n]
    def size(self,n):
        return -self.Parent[self.root(n)]
u=UnionFind(N)
for c,d in CD:
    u.unite(c-1,d-1)
from collections import defaultdict
d=defaultdict(int)
d2=defaultdict(int)
for i in range(N):
    d[u.root(i)]+=A[i]
    d2[u.root(i)]+=B[i]
print(['No','Yes'][all(d[k]==d2[k] for k in d)])
