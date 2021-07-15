import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
n=int(input())
points=[list(map(int,input().split()))+[i] for i in range(n)]
points.sort(key = lambda x:x[1])
edge=[]
for i in range(n-1):
    edge.append((points[i][2],points[i+1][2],points[i+1][1]-points[i][1]))
points.sort()
for i in range(n-1):
    edge.append((points[i][2],points[i+1][2],points[i+1][0]-points[i][0]))
class UnionFind(object):
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1 for i in range(N)]
    
    def merge(self, a, b):
        if self.issame(a,b):
            return
        pa = self.root(a)
        pb = self.root(b)
        self.parent[pa] = pb
        self.size[pb] += self.size[pa]
    def root(self, x):
        p = self.parent[x]
        if p == x:
            return x
        else:
            r = self.root(p)
            self.parent[x] = r
            return r
    
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    def getsize(self, x):
        return self.size[self.root(x)]
edge.sort(key=lambda x:x[2])
uf=UnionFind(n)
ans=0
for ed in edge:
    if uf.issame(ed[0],ed[1]):continue
    ans+=ed[2]
    uf.merge(ed[0],ed[1])
print(ans)
