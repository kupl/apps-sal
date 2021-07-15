import sys
class UF():
    def __init__(self, num):
        self.par = [-1]*num
        self.size = [1]*num
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            x = self.par[x]
            return self.find(x)
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] < self.par[ry]:
                self.par[ry] = rx
                self.size[rx] += self.size[ry] 
            elif self.par[rx] > self.par[ry]:
                self.par[rx] = ry
                self.size[ry] += self.size[rx]
            else:
                self.par[rx] -= 1
                self.par[ry] = rx
                self.size[rx] += self.size[ry]
        return

def solve():
    N, M = map(int, sys.stdin.readline().split())
    G = UF(N)
    for _ in range(M):
        L = list(map(int, sys.stdin.readline().split()))
        if L[0] > 1:
            l = L[1]
            for r in L[2:]:
                G.union(l-1, r-1)
    Ans = [0]*N
    for i in range(N):
        Ans[i] = G.size[G.find(i)]
    print(*Ans)
def __starting_point():
    solve()
__starting_point()
