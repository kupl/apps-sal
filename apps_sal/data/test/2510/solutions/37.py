class Unionfind:
    def __init__(self,n):
        self.par=[x for x in range(n)]
        self.num=[1]*n

    def root(self,a):
        if self.par[a]==a : return a
        parent=self.root(self.par[a])
        self.par[a]=parent
        return parent

    def unite(self,a,b):
        ra,rb=self.root(a),self.root(b)
        self.par[rb]=ra
        self.num[ra]+=self.num[rb]

    def same(self,a,b):
        return self.root(a)==self.root(b)



def main():
    n,m=map(int,input().split())
    uf=Unionfind(n)

    for _ in range(m):
        a,b=map(int,input().split())
        if uf.same(a-1,b-1) : continue
        uf.unite(a-1,b-1)

    print(max(uf.num))

main()
