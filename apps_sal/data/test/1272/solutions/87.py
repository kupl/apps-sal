from collections import defaultdict

class UnionFind():
    def __init__(self, n=0):
        self.d = [-1]*n
        self.g = set()
    
    def find(self, x):
        if self.d[x] < 0: return x
        self.d[x] = self.find(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        x,y=self.find(x),self.find(y)
        if x==y:return False
        if self.d[x] > self.d[y]: x,y=y,x
        self.d[x] += self.d[y]
        self.g.add(x)
        if y in self.g:self.g.remove(y)
        self.d[y] = x
        return True

    def same(self,x,y): return self.find(x)==self.find(y)
    def size(self,x): return -self.d[self.find(x)]
    
def comb2(n):
  return n*(n-1)//2
    
N,M=map(int,input().split())
E = [tuple(map(int,input().split())) for _ in range(M)]

total=comb2(N)
uf = UnionFind(N+1)
ans = [total]
for i in range(M-1):
  a,b = E[-i-1]
  if uf.same(a,b):
    ans.append(ans[-1])
    continue
  else:
    size1,size2 = uf.size(a),uf.size(b)
    uf.unite(a,b)
    size3 = uf.size(a)
    tmp = ans[-1]+comb2(size1)+comb2(size2)-comb2(size3)
    ans.append(tmp)
print(*ans[::-1])
