import sys
sys.setrecursionlimit(10**7)
from collections import Counter
class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n

    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
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
    #木の深さじゃなくxを含む集合の要素数
    def size(self,x):
        return -self.parents[self.find(x)]

    def same(self,x,y):
        return self.find(x)==self.find(y)

    def members(self,x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i)==root]

    def roots(self):
        return [i for i,x in enumerate(self.parents) if x>0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
n,k,l=map(int,input().split())
load=UnionFind(n+1)
tetsu=UnionFind(n+1)
for _ in range(k):
    p,q=map(int,input().split())
    load.union(p,q)
for _ in range(l):
    r,s = map(int,input().split())
    tetsu.union(r,s)

count = [(load.find(i),tetsu.find(i)) for i in range(1,n+1)]
# print(count)
C = Counter(count)
ans = []
for i in range(n):
	if count[i][0]<0 or count[i][1]<0:
		ans.append(0)
	else:
		ans.append(C[count[i]])
print(*ans)
