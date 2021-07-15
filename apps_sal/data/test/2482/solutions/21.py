import collections
class UnionFind:
    def __init__(self,n):
        super().__init__()
        self.par = [-1]*n
        self.rank = [0]*n
        self.tsize = [1]*n

    
    def root(self,x):
        if self.par[x] == -1:
            return x 
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x_r = self.root(x)
        y_r = self.root(y)
        
        if self.rank[x_r]>self.rank[y_r]:
            self.par[y_r] = x_r

        elif self.rank[x_r]<self.rank[y_r]:
            self.par[x_r] = y_r

        elif x_r != y_r:
            self.par[y_r] = x_r
            self.rank[x_r] += 1

        if x_r != y_r:
            size = self.tsize[x_r]+self.tsize[y_r]
            self.tsize[x_r] = size
            self.tsize[y_r] = size

    def isSame(self,x,y):
        return self.root(x) == self.root(y)

    def size(self,x):
        return self.tsize[self.root(x)]

def main():
    n,k,l = tuple([int(t)for t in input().split()])

    uf_k = UnionFind(n)
    uf_l = UnionFind(n)


    pq = [[int(t)-1 for t in input().split()]for _ in [0]*k]
    for p,q in pq:
        uf_k.unite(p,q)

    rs = [[int(t)-1 for t in input().split()]for _ in [0]*l]
    for r,s in rs:
        uf_l.unite(r,s)

    pair = []
    for i in range(n):
        pair.append((uf_k.root(i),uf_l.root(i)))
    counter = collections.Counter(pair)
    
    ans = []
    for a in pair:
        ans.append(counter[a])
    print(*ans)
    
def __starting_point():
    main()
__starting_point()
