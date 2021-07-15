class UnionFind():    
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n
        self.rnk = [0] * n
        
    def findRoot(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.findRoot(self.root[x])  #; print('root[x]', self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.findRoot(x)
        y = self.findRoot(y)
        if x == y:
            return 
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSame(self, x, y):
        return self.findRoot(x) == self.findRoot(y)
    
    def count(self, x):
        return -self.root[self.findRoot(x)]

    
def nC2(n):
    return n*(n-1) // 2 


from itertools import accumulate

N, M =  map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(M)]  #;print(edge)

comb = []
uf = UnionFind(N+1)
for eg in edge[::-1]:
    if not uf.isSame(eg[0], eg[1]):
        pre0 = uf.count(eg[0])
        pre1 = uf.count(eg[1])
        uf.unite(eg[0], eg[1])
        post = uf.count(eg[0])
        #print(eg[0], eg[1], pre0, pre1, post, nC2(pre0), nC2(pre1), nC2(post) )
        comb.append(nC2(post) - (nC2(pre0)+nC2(pre1)))
    else:
        comb.append(0)            
#print(comb)
for i in accumulate(comb[::-1]):
    print(i)
