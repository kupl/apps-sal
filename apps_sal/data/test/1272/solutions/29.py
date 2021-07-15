import sys

input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1]*(n+1)#それぞれの要素がどの要素の子であるか

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]#それぞれの要素の根を再帰的に求める

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        
        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)#x,yが同じ集合に属するかどうか
    
    def size(self, x):
        return -self.par[self.find(x)]
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if root == self.find(i)]        

def main():
    n, m = list(map(int, input().split()))
    bridge = [None]*m
    for i in range(m):
        bridge[i] = [int(x) for x in input().split()]
    
    union = UnionFind(n)
    
    ans = [0]*m
    for i in range(m):
        a, b = bridge[m-1-i][0], bridge[m-1-i][1]
        if union.same(a, b) == False:
        	ans[i] = union.size(a)*union.size(b)
        if i != 0:
            ans[i] += ans[i-1]
        union.union(a, b)
    
    for i in range(1, m):
        print((n*(n-1)//2-ans[m-1-i]))
    print((n*(n-1)//2))
        
def __starting_point():
    main()


__starting_point()
