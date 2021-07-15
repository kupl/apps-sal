import math

class UF:
    def __init__(self, N):
        self.p = list(range(N))
        self.size = [1] * N
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            sx, sy = self.size[px], self.size[py]
            if sx < sy:
                self.p[px] = py
                self.size[py] += sx
            else:
                self.p[py] = px
                self.size[px] += sy
        
class Solution:
    def largestComponentSize(self, a: List[int]) -> int:
        d = {}
        uf = UF(len(a))
        for i, n in enumerate(a):
            for f in range(2, int(math.sqrt(n)+ 1)):
                if n % f == 0:
                    for ff in [f, n//f]:
                        if ff in d:
                            uf.union(i, d[ff])
                        else:
                            d[ff] = i
            if n not in d:
                d[n] = i
            else:
                uf.union(i, d[n])
        return max(uf.size)
            

