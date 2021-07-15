from collections import defaultdict as dd

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n

    def find(self, x):
        if self.root[x-1] < 0:
            return x
        else:
            self.root[x-1] = self.find(self.root[x-1])
            return self.root[x-1]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        elif self.rank[x-1] > self.rank[y-1]:
            self.n-=1
            self.root[x-1] += self.root[y-1]
            self.root[y-1] = x
        else:
            self.n-=1
            self.root[y-1] += self.root[x-1]
            self.root[x-1] = y
            if self.rank[x-1] == self.rank[y-1]:
                self.rank[y-1] += 1

    def same(self, x, y):
        return self.find(x)==self.find(y)

    def count(self, x):
        return -self.root[self.find(x)-1]

    def size(self):
        return self.n

def main():
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    uf=UnionFind(n)
    for _ in range(m): uf.unite(*map(int,input().split()))
    s=dd(int)
    t=dd(int)
    for i in range(n):
        ii=uf.find(i+1)
        s[ii]+=A[i]
        t[ii]+=B[i]
    for k in s.keys():
        if s[k]==t[k]: continue
        else:
            print('No')
            break
    else: print('Yes')

main()
